import os
import tempfile
import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import pytest
from src.pipeline.extract import extract_from_excel


class TestExtractFromExcel(unittest.TestCase):
    """Testes para a função extract_from_excel."""

    def setUp(self):
        """Configuração inicial para os testes."""
        # Criar um diretório temporário para os testes
        self.temp_dir = tempfile.mkdtemp()
        
    def tearDown(self):
        """Limpeza após cada teste."""
        # Remover diretório temporário e seus conteúdos
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    @patch('glob.glob')
    @patch('pandas.read_excel')
    def test_extract_from_excel_with_files(self, mock_read_excel, mock_glob):
        """Testa extração com arquivos Excel existentes."""
        # Configurar mocks
        mock_glob.return_value = ['file1.xlsx', 'file2.xlsx']
        
        # Criar DataFrames de teste
        df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
        df2 = pd.DataFrame({'C': [5, 6], 'D': [7, 8]})
        mock_read_excel.side_effect = [df1, df2]
        
        # Executar função
        result = extract_from_excel('test/path')
        
        # Verificações
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], pd.DataFrame)
        self.assertIsInstance(result[1], pd.DataFrame)
        
        # Verificar se pandas.read_excel foi chamado para cada arquivo
        self.assertEqual(mock_read_excel.call_count, 2)
        mock_read_excel.assert_any_call('file1.xlsx')
        mock_read_excel.assert_any_call('file2.xlsx')

    @patch('glob.glob')
    def test_extract_from_excel_no_files(self, mock_glob):
        """Testa extração quando não há arquivos Excel."""
        # Configurar mock para retornar lista vazia
        mock_glob.return_value = []
        
        # Executar função
        result = extract_from_excel('empty/path')
        
        # Verificações
        self.assertEqual(result, [])
        self.assertIsInstance(result, list)

    @patch('glob.glob')
    @patch('pandas.read_excel')
    def test_extract_from_excel_single_file(self, mock_read_excel, mock_glob):
        """Testa extração com um único arquivo Excel."""
        # Configurar mocks
        mock_glob.return_value = ['single_file.xlsx']
        df = pd.DataFrame({'name': ['Alice', 'Bob'], 'age': [25, 30]})
        mock_read_excel.return_value = df
        
        # Executar função
        result = extract_from_excel('single/path')
        
        # Verificações
        self.assertEqual(len(result), 1)
        pd.testing.assert_frame_equal(result[0], df)

    @patch('glob.glob')
    @patch('pandas.read_excel')
    def test_extract_from_excel_pandas_exception(self, mock_read_excel, mock_glob):
        """Testa comportamento quando pandas.read_excel levanta exceção."""
        # Configurar mocks
        mock_glob.return_value = ['corrupted_file.xlsx']
        mock_read_excel.side_effect = Exception("Arquivo corrompido")
        
        # Verificar se a exceção é propagada
        with self.assertRaises(Exception):
            extract_from_excel('test/path')

    @patch('glob.glob')
    def test_extract_from_excel_correct_pattern(self, mock_glob):
        """Testa se o padrão correto é usado para buscar arquivos."""
        mock_glob.return_value = []
        
        # Executar função
        extract_from_excel('test/input/path')
        
        # Verificar se glob foi chamado com o padrão correto
        expected_pattern = os.path.join('test/input/path', '*.xlsx')
        mock_glob.assert_called_once_with(expected_pattern)

    @patch('glob.glob')
    @patch('pandas.read_excel')
    def test_extract_from_excel_dataframe_content(self, mock_read_excel, mock_glob):
        """Testa se o conteúdo dos DataFrames é preservado corretamente."""
        # Configurar mocks
        mock_glob.return_value = ['test_file.xlsx']
        
        # Criar DataFrame de teste com dados específicos
        test_data = pd.DataFrame({
            'id': [1, 2, 3],
            'nome': ['João', 'Maria', 'Pedro'],
            'idade': [25, 30, 35],
            'salario': [5000.0, 6000.0, 7000.0]
        })
        mock_read_excel.return_value = test_data
        
        # Executar função
        result = extract_from_excel('test/path')
        
        # Verificações detalhadas
        self.assertEqual(len(result), 1)
        returned_df = result[0]
        
        # Verificar estrutura do DataFrame
        self.assertEqual(list(returned_df.columns), ['id', 'nome', 'idade', 'salario'])
        self.assertEqual(len(returned_df), 3)
        
        # Verificar dados específicos
        self.assertEqual(returned_df.iloc[0]['nome'], 'João')
        self.assertEqual(returned_df.iloc[1]['idade'], 30)
        self.assertEqual(returned_df.iloc[2]['salario'], 7000.0)

    def test_extract_from_excel_input_path_validation(self):
        """Testa se a função aceita diferentes tipos de caminhos."""
        with patch('glob.glob') as mock_glob:
            mock_glob.return_value = []
            
            # Testar com diferentes formatos de caminho
            paths_to_test = [
                'data/input',
                './data/input',
                '../data/input',
                'C:/data/input',  # Windows absolute path
                '/data/input'     # Unix-style path
            ]
            
            for path in paths_to_test:
                result = extract_from_excel(path)
                self.assertIsInstance(result, list)


if __name__ == '__main__':
    unittest.main()