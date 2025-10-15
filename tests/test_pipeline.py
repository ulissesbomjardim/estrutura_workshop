import runpy
import sys
import types

import pytest

# cria um dicionário para capturar chamadas
called = {}

def test_main_executes_pipeline_and_prints_messages(monkeypatch, capsys):
    # mocks das funções do pipeline
    def mock_extract(path):
        called['extract'] = path
        return ['r1', 'r2']

    def mock_transform(data_list):
        called['transform'] = data_list
        return "df_concatenado"

    def mock_load(df, output_path, filename):
        called['load'] = (df, output_path, filename)
        return "arquivo xlsx salvo com sucesso"

    # cria módulos pipeline e submódulos e insere em sys.modules via monkeypatch
    pipeline_pkg = types.ModuleType('pipeline')
    pipeline_pkg.__path__ = []  # marca como package
    monkeypatch.setitem(sys.modules, 'pipeline', pipeline_pkg)

    mod_ext = types.ModuleType('pipeline.extract')
    mod_ext.extract_fron_excel = mock_extract
    monkeypatch.setitem(sys.modules, 'pipeline.extract', mod_ext)

    mod_trans = types.ModuleType('pipeline.transform')
    mod_trans.transform_data = mock_transform
    monkeypatch.setitem(sys.modules, 'pipeline.transform', mod_trans)

    mod_load = types.ModuleType('pipeline.load')
    mod_load.load_to_excel = mock_load
    monkeypatch.setitem(sys.modules, 'pipeline.load', mod_load)

    # executa o script como "__main__"
    runpy.run_path("src/main.py", run_name="__main__")

    # asserts sobre chamadas
    assert called['extract'] == "data/input"
    assert called['transform'] == ['r1', 'r2']
    assert called['load'] == ("df_concatenado", "data/output", "dados_concatenados")

    # verifica saída impressa
    out = capsys.readouterr().out
    assert "<class 'list'>" in out
    assert "<class 'str'>" in out
    assert "arquivo xlsx salvo com sucesso" in out