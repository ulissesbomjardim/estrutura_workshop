# 🧪 Tests — Testes Automatizados

Esta página documenta os testes existentes no projeto, explica como executá-los e interpretar os resultados.

---

## 🎯 Visão Geral dos Testes

O projeto utiliza **pytest** para testes automatizados, garantindo:

- ✅ **Qualidade do código**
- ✅ **Funcionamento correto das funções**
- ✅ **Prevenção de regressões**
- ✅ **Cobertura de código**

---

## 🚀 Executando os Testes

### ⚡ Execução Rápida:
```bash
# Usando task do Poetry (recomendado)
poetry run task test
```

### 🔧 Execução Manual:
```bash
# Todos os testes (modo silencioso)
poetry run pytest -q

# Todos os testes (modo verboso)
poetry run pytest -vv

# Testes com cobertura
poetry run pytest --cov=src

# Teste específico
poetry run pytest tests/test_transform.py -q
```

### 🔍 Comandos Úteis:
```bash
# Apenas testes que contêm "transform"
poetry run pytest -k transform -q

# Parar no primeiro erro
poetry run pytest -x

# Executar em paralelo (se instalado pytest-xdist)
poetry run pytest -n auto
```

---

## 📁 Estrutura dos Testes

```
tests/
├── 🧪 test_extract.py      # Testes do módulo de extração
├── 🔄 test_transform.py    # Testes do módulo de transformação
├── 📤 test_load.py         # Testes do módulo de carregamento
└── 🔗 test_pipeline.py     # Teste de integração completa
```

---

## 🔄 test_transform.py

### 🎯 **Objetivo**: Validar a função `transform_data` (concatenação de DataFrames)

### ✅ **Testes Incluídos**:

#### 📊 `test_concat_two_dataframes`
- **Verifica**: Concatenação de dois DataFrames com mesmas colunas
- **Compara**: Resultado com `pd.concat` esperado

#### 📋 `test_single_dataframe_returns_same_dataframe`
- **Verifica**: Lista com único DataFrame retorna igual
- **Garante**: Comportamento correto com entrada mínima

#### ❌ `test_empty_list_raises_value_error`
- **Verifica**: Lista vazia lança `ValueError`
- **Valida**: Tratamento de erro adequado

#### 🔀 `test_concat_different_columns_creates_union_and_fills_nan`
- **Verifica**: Concatenação com colunas diferentes
- **Valida**: União de colunas e preenchimento com NaN

### 🔍 **Dicas de Depuração**:
```bash
# Executar apenas testes de transform
poetry run pytest -k transform -vv
```

---

## 📤 test_load.py

### 🎯 **Objetivo**: Validar a função `load_to_excel` (salvamento em Excel)

### ✅ **Testes Incluídos**:

#### 💾 `test_load_to_excel_creates_file_and_returns_message`
- **Verifica**: Arquivo é criado corretamente
- **Valida**: Mensagem de sucesso retornada
- **Compara**: Arquivo salvo vs DataFrame original

#### 📁 `test_load_to_excel_creates_nested_dir_if_missing`
- **Verifica**: Criação automática de diretórios
- **Usa**: `tmp_path` para testes isolados

### 🔧 **Sobre tmp_path**:
- **Fixture do pytest** que cria diretório temporário
- **Isolamento**: Cada teste tem seu próprio diretório
- **Limpeza**: Removido automaticamente após o teste

---

## 📥 test_extract.py

### 🎯 **Objetivo**: Validar a função `extract_from_excel` (leitura de Excel)

### ✅ **Testes Incluídos**:
- Leitura de arquivos Excel válidos
- Tratamento de diretórios vazios
- Validação do formato de retorno

---

## 🔗 test_pipeline.py

### 🎯 **Objetivo**: Teste de integração do pipeline completo

### 🎭 **Abordagem com Mocks**:
- **Usa**: `monkeypatch` para injetar mocks
- **Executa**: `src/main.py` completo via `runpy.run_path`
- **Verifica**: Chamadas corretas para funções do pipeline
- **Valida**: Saída impressa no console

### 🔄 **Por que usar mocks?**:
- ✅ **Velocidade**: Evita I/O real de arquivos
- ✅ **Determinismo**: Resultados previsíveis
- ✅ **Isolamento**: Testa apenas a lógica de orquestração

---

## 📊 Interpretando Resultados

### ✅ **Sucesso**:
```bash
======================== 8 passed in 0.45s ========================
```

### ❌ **Falha**:
```bash
FAILED tests/test_transform.py::test_concat_two_dataframes - AssertionError
```

### 📈 **Com Cobertura**:
```bash
---------- coverage: platform win32, python 3.12.7 -----------
Name                     Stmts   Miss  Cover
--------------------------------------------
src\main.py                 10      0   100%
src\pipeline\extract.py     15      2    87%
src\pipeline\load.py        12      0   100%
src\pipeline\transform.py    8      0   100%
--------------------------------------------
TOTAL                       45      2    96%
```

---

## 🛠️ Adicionando Novos Testes

### 📋 **Boas Práticas**:

#### 🔧 Use fixtures do pytest:
```python
def test_example(tmp_path):
    # tmp_path cria diretório temporário
    test_file = tmp_path / "test.xlsx"
```

#### 📊 Crie DataFrames pequenos:
```python
df = pd.DataFrame({"col1": [1, 2], "col2": ["a", "b"]})
```

#### ✅ Use asserts específicos:
```python
import pandas.testing as pdt
pdt.assert_frame_equal(result, expected)
```

---

## 🚀 Integração com CI/CD

Os testes são executados automaticamente:

- 🔄 **Em cada commit** (via GitHub Actions)
- 📊 **Com relatório de cobertura** (Codecov)
- ✅ **Antes de merge** (proteção de branch)

Veja mais detalhes em [🚀 CI](ci.md).

---

## 🔗 Próximos Passos

- 🚀 **Execute o Pipeline**: [📋 Pipeline](pipeline.md)
- 💻 **Explore o Código**: [📖 Documentação do Código](codigo.md)
- 🔧 **Configure CI**: [🚀 CI](ci.md)
