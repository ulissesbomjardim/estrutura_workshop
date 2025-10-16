# ⚙️ Transform — Módulo de Transformação

Este módulo é responsável pela transformação e consolidação dos dados extraídos no pipeline ETL.

---

## 🎯 Visão Geral

O módulo `transform.py` é o segundo estágio do pipeline ETL, responsável por:

- 🔄 **Concatenar** múltiplos DataFrames em um único
- ✅ **Validar** dados de entrada
- 🧹 **Limpar** e organizar estrutura dos dados
- 📊 **Preparar** dados para carregamento

---

## 🔧 Funcionalidades

### ✅ **Capacidades**:
- 🔗 Concatenação eficiente com pandas
- 🔍 Validação de entrada (lista não vazia)
- 📋 Preservação de estrutura de colunas
- 🧹 Reset automático de índices

### ⚡ **Performance**:
- 🚀 Operação otimizada com `pd.concat()`
- 💾 Uso eficiente de memória
- 🔄 Processamento em lote

---

## 📖 Documentação da API

### 🎯 **Função Principal**

::: src.pipeline.transform.transform_data

---

## 💻 Exemplos de Uso

### 🔄 **Uso Básico**
```python
from pipeline.transform import transform_data
import pandas as pd

# Dados de exemplo
df1 = pd.DataFrame({"nome": ["Ana", "Bruno"], "idade": [25, 30]})
df2 = pd.DataFrame({"nome": ["Carlos", "Diana"], "idade": [35, 28]})

# Concatenar DataFrames
resultado = transform_data([df1, df2])
print(resultado)
#      nome  idade
# 0     Ana     25
# 1   Bruno     30
# 2  Carlos     35
# 3   Diana     28
```

### 🔍 **Validação de Entrada**
```python
# Lista vazia gera erro
try:
    resultado = transform_data([])
except ValueError as e:
    print(f"❌ Erro: {e}")
    # Saída: Erro: data_list must contain at least one DataFrame

# Lista válida
data_list = [df1, df2]
if data_list:
    resultado = transform_data(data_list)
    print(f"✅ Dados consolidados: {resultado.shape}")
```

### 🔀 **Colunas Diferentes**
```python
# DataFrames com colunas diferentes
df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
df2 = pd.DataFrame({"B": [5, 6], "C": [7, 8]})

resultado = transform_data([df1, df2])
print(resultado)
#      A    B    C
# 0  1.0    3  NaN
# 1  2.0    4  NaN
# 2  NaN    5  7.0
# 3  NaN    6  8.0
```

---

## 🔄 Fluxo de Execução

```mermaid
graph LR
    A[📋 Lista DataFrames] --> B{🔍 Lista Vazia?}
    B -->|✅ Não| C[🔗 pd.concat()]
    B -->|❌ Sim| D[🚫 ValueError]
    C --> E[📊 ignore_index=True]
    E --> F[📤 DataFrame Final]

    style A fill:#e3f2fd
    style C fill:#f3e5f5
    style F fill:#e8f5e8
    style D fill:#ffebee
```

---

## ⚙️ Comportamento Detalhado

### 🔗 **Concatenação**
- **Método**: `pd.concat(data_list, ignore_index=True)`
- **Eixo**: Vertical (linhas) - `axis=0` (padrão)
- **Índices**: Reset automático com `ignore_index=True`
- **Junção**: Outer join (união de todas as colunas)

### 📊 **Tratamento de Colunas**
- **Colunas iguais**: Dados concatenados normalmente
- **Colunas diferentes**: União de todas + preenchimento com `NaN`
- **Ordem**: Preservada conforme aparição nos DataFrames

### 🧹 **Limpeza de Dados**
- **Índices**: Reset para sequência 0, 1, 2, ...
- **Tipos**: Preservados quando possível
- **NaN**: Preenchimento automático para colunas ausentes

---

## 🛠️ Validação e Tratamento de Erros

### ✅ **Validações Implementadas**

#### 📋 **Lista vazia**
```python
if not data_list:
    raise ValueError("data_list must contain at least one DataFrame")
```

### ❌ **Cenários de Erro**

#### 📄 **Tipo incorreto**
```python
# Erro: item não é DataFrame
try:
    resultado = transform_data([df1, "não é dataframe"])
except AttributeError as e:
    print(f"❌ Tipo inválido: {e}")
```

#### 🔄 **DataFrames vazios**
```python
# DataFrame vazio é aceito
df_vazio = pd.DataFrame()
resultado = transform_data([df1, df_vazio])
# Resultado: apenas dados de df1
```

---

## 🚀 Melhorias Possíveis

### 🔧 **Validação Avançada**
```python
def transform_data_enhanced(data_list: List[pd.DataFrame]) -> pd.DataFrame:
    """Versão com validações extras"""

    # Validar entrada
    if not data_list:
        raise ValueError("Lista não pode estar vazia")

    # Validar tipos
    for i, df in enumerate(data_list):
        if not isinstance(df, pd.DataFrame):
            raise TypeError(f"Item {i} não é DataFrame")

    # Filtrar DataFrames vazios
    valid_dfs = [df for df in data_list if not df.empty]

    if not valid_dfs:
        raise ValueError("Todos os DataFrames estão vazios")

    return pd.concat(valid_dfs, ignore_index=True)
```

### 📊 **Schema Validation**
```python
def validate_common_schema(data_list: List[pd.DataFrame]) -> bool:
    """Verifica se todos DataFrames têm as mesmas colunas"""

    if not data_list:
        return False

    base_columns = set(data_list[0].columns)

    for df in data_list[1:]:
        if set(df.columns) != base_columns:
            return False

    return True
```

### 🧹 **Limpeza de Dados**
```python
def transform_with_cleaning(data_list: List[pd.DataFrame]) -> pd.DataFrame:
    """Transformação com limpeza básica"""

    result = transform_data(data_list)

    # Remover linhas completamente vazias
    result = result.dropna(how='all')

    # Remover duplicatas
    result = result.drop_duplicates()

    # Reset do índice
    result = result.reset_index(drop=True)

    return result
```

---

## 📊 Casos de Uso Avançados

### 🔀 **Concatenação com Identificador**
```python
def transform_with_source(data_list: List[pd.DataFrame],
                         source_names: List[str]) -> pd.DataFrame:
    """Adiciona coluna identificando fonte dos dados"""

    dfs_with_source = []
    for df, source in zip(data_list, source_names):
        df_copy = df.copy()
        df_copy['fonte'] = source
        dfs_with_source.append(df_copy)

    return pd.concat(dfs_with_source, ignore_index=True)
```

### 🎯 **Concatenação Seletiva**
```python
def transform_specific_columns(data_list: List[pd.DataFrame],
                              columns: List[str]) -> pd.DataFrame:
    """Concatena apenas colunas específicas"""

    filtered_dfs = []
    for df in data_list:
        # Selecionar apenas colunas que existem
        available_cols = [col for col in columns if col in df.columns]
        if available_cols:
            filtered_dfs.append(df[available_cols])

    return pd.concat(filtered_dfs, ignore_index=True)
```

---

## 🧪 Testes

### 📋 **Testes Incluídos**
- ✅ Concatenação de dois DataFrames iguais
- ✅ DataFrame único retorna igual
- ✅ Lista vazia gera ValueError
- ✅ Colunas diferentes criam união + NaN

### 🔧 **Executar Testes**
```bash
# Testes específicos do módulo transform
poetry run pytest tests/test_transform.py -v

# Com cobertura
poetry run pytest tests/test_transform.py --cov=src.pipeline.transform
```

### 🧪 **Teste Manual**
```python
# Teste rápido da função
from pipeline.transform import transform_data
import pandas as pd

# Criar dados de teste
df1 = pd.DataFrame({"x": [1, 2], "y": [3, 4]})
df2 = pd.DataFrame({"x": [5, 6], "y": [7, 8]})

# Testar transformação
result = transform_data([df1, df2])
assert len(result) == 4
assert list(result.columns) == ["x", "y"]
print("✅ Teste manual passou!")
```

---

## 🔗 Próximos Passos

- 📤 **Load**: [📤 Load](load.md) - Próximo estágio do pipeline
- 📥 **Extract**: [📥 Extract](extract.md) - Estágio anterior
- 🎯 **Main**: [🎯 Main](main.md) - Orquestração completa
- 📖 **Overview**: [📖 Código](codigo.md) - Visão geral da arquitetura
