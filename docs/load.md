# 📤 Load — Módulo de Carregamento

Este módulo é responsável pelo carregamento e persistência dos dados transformados no pipeline ETL.

---

## 🎯 Visão Geral

O módulo `load.py` é o terceiro e último estágio do pipeline ETL, responsável por:

- 💾 **Salvar** DataFrames em arquivos Excel
- 📁 **Criar** diretórios de saída automaticamente
- ✅ **Confirmar** sucesso da operação
- 🔧 **Configurar** formato de saída

---

## 🔧 Funcionalidades

### ✅ **Capacidades**:
- 📊 Salvamento em formato Excel (.xlsx)
- 📁 Criação automática de diretórios
- 🏷️ Nomeação personalizada de arquivos
- ✅ Confirmação de sucesso

### ⚡ **Performance**:
- 🚀 Escrita otimizada com openpyxl
- 📁 Operações eficientes de sistema de arquivos
- 💾 Controle de memória durante salvamento

---

## 📖 Documentação da API

### 🎯 **Função Principal**

::: src.pipeline.load.load_to_excel

---

## 💻 Exemplos de Uso

### 💾 **Uso Básico**
```python
from pipeline.load import load_to_excel
import pandas as pd

# Criar DataFrame de exemplo
df = pd.DataFrame({
    "nome": ["Ana", "Bruno", "Carlos"],
    "idade": [25, 30, 35],
    "cidade": ["SP", "RJ", "BH"]
})

# Salvar em Excel
mensagem = load_to_excel(
    df=df,
    output_path="data/output",
    filename="dados_processados"
)
print(mensagem)  # "arquivo xlsx salvo com sucesso"
```

### 📁 **Criação de Diretórios**
```python
# Diretório será criado automaticamente
mensagem = load_to_excel(
    df=df,
    output_path="data/novapasta/subpasta",
    filename="relatorio"
)
# Cria toda a estrutura: data/novapasta/subpasta/
```

### 🏷️ **Nomes de Arquivo Personalizados**
```python
from datetime import datetime

# Nome com timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"dados_{timestamp}"

mensagem = load_to_excel(df, "data/output", filename)
# Salva como: dados_20241016_143022.xlsx
```

---

## 🔄 Fluxo de Execução

```mermaid
graph LR
    A[📊 DataFrame] --> B[📁 Verificar Diretório]
    B --> C{🔍 Existe?}
    C -->|❌ Não| D[📁 Criar Diretório]
    C -->|✅ Sim| E[📝 Construir Caminho]
    D --> E
    E --> F[💾 df.to_excel()]
    F --> G[✅ Retornar Sucesso]

    style A fill:#e3f2fd
    style D fill:#f3e5f5
    style F fill:#fff3e0
    style G fill:#e8f5e8
```

---

## ⚙️ Comportamento Detalhado

### 📁 **Gerenciamento de Diretórios**
- **Método**: `os.makedirs(output_path, exist_ok=True)`
- **Recursivo**: Cria toda a estrutura necessária
- **Seguro**: `exist_ok=True` evita erro se já existir

### 💾 **Salvamento**
- **Engine**: `openpyxl` (padrão para .xlsx)
- **Índices**: `index=False` (não salva índices do DataFrame)
- **Formato**: Excel nativo (.xlsx)
- **Codificação**: UTF-8 (padrão do pandas)

### 🔧 **Configurações**
- **Extensão**: Adicionada automaticamente (.xlsx)
- **Sobrescrita**: Arquivos existentes são substituídos
- **Permissões**: Dependem do sistema operacional

---

## 🛠️ Tratamento de Erros

### ❌ **Cenários de Erro Comuns**

#### 🔒 **Arquivo em uso (Windows)**
```python
# Problema: arquivo aberto no Excel
try:
    mensagem = load_to_excel(df, "data/output", "planilha")
except PermissionError:
    print("❌ Feche o arquivo no Excel e tente novamente")
```

#### 📁 **Permissões de diretório**
```python
try:
    mensagem = load_to_excel(df, "/sistema/protegido", "arquivo")
except PermissionError:
    print("❌ Sem permissão para escrever no diretório")
```

#### 💾 **Espaço em disco**
```python
try:
    mensagem = load_to_excel(df, "data/output", "arquivo_grande")
except OSError as e:
    print(f"❌ Erro de sistema: {e}")
```

---

## 🚀 Melhorias Possíveis

### 🔧 **Validação de Entrada**
```python
def load_to_excel_enhanced(df: pd.DataFrame,
                          output_path: str,
                          filename: str) -> str:
    """Versão com validações extras"""

    # Validar DataFrame
    if df.empty:
        raise ValueError("DataFrame está vazio")

    # Validar nome do arquivo
    invalid_chars = '<>:"/\\|?*'
    if any(char in filename for char in invalid_chars):
        raise ValueError(f"Nome inválido: {filename}")

    # Salvamento normal
    return load_to_excel(df, output_path, filename)
```

### 📊 **Múltiplos Formatos**
```python
def save_multiple_formats(df: pd.DataFrame,
                         output_path: str,
                         filename: str) -> Dict[str, str]:
    """Salva em múltiplos formatos"""

    results = {}

    # Excel
    excel_msg = load_to_excel(df, output_path, filename)
    results['excel'] = excel_msg

    # CSV
    csv_path = os.path.join(output_path, f"{filename}.csv")
    df.to_csv(csv_path, index=False)
    results['csv'] = "arquivo csv salvo com sucesso"

    # Parquet
    parquet_path = os.path.join(output_path, f"{filename}.parquet")
    df.to_parquet(parquet_path, index=False)
    results['parquet'] = "arquivo parquet salvo com sucesso"

    return results
```

### 🎨 **Formatação Excel**
```python
def load_to_excel_formatted(df: pd.DataFrame,
                           output_path: str,
                           filename: str) -> str:
    """Salva com formatação Excel"""

    os.makedirs(output_path, exist_ok=True)
    file_path = os.path.join(output_path, f"{filename}.xlsx")

    # Usar ExcelWriter para formatação
    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Dados', index=False)

        # Ajustar largura das colunas
        worksheet = writer.sheets['Dados']
        for column in worksheet.columns:
            max_length = 0
            column_letter = column[0].column_letter

            for cell in column:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))

            adjusted_width = min(max_length + 2, 50)
            worksheet.column_dimensions[column_letter].width = adjusted_width

    return "arquivo xlsx formatado salvo com sucesso"
```

---

## 📊 Formatos de Saída

### ✅ **Formato Principal**
- **Excel (.xlsx)**: Formato padrão da função

### 🔄 **Formatos Alternativos**
```python
# CSV (mais leve)
df.to_csv(os.path.join(output_path, f"{filename}.csv"), index=False)

# Parquet (mais eficiente)
df.to_parquet(os.path.join(output_path, f"{filename}.parquet"), index=False)

# JSON (intercâmbio)
df.to_json(os.path.join(output_path, f"{filename}.json"), orient='records')
```

### 🎯 **Escolha do Formato**
- **Excel**: Melhor para análise manual
- **CSV**: Melhor para sistemas legados
- **Parquet**: Melhor para big data
- **JSON**: Melhor para APIs

---

## 🧪 Testes

### 📋 **Testes Incluídos**
- ✅ Criação de arquivo e mensagem de sucesso
- ✅ Verificação de conteúdo salvo
- ✅ Criação automática de diretórios
- ✅ Tratamento de caminhos aninhados

### 🔧 **Executar Testes**
```bash
# Testes específicos do módulo load
poetry run pytest tests/test_load.py -v

# Com cobertura
poetry run pytest tests/test_load.py --cov=src.pipeline.load
```

### 🧪 **Teste Manual**
```python
# Teste rápido da função
from pipeline.load import load_to_excel
import pandas as pd
import os

# Criar dados de teste
df = pd.DataFrame({"col1": [1, 2], "col2": ["a", "b"]})

# Testar salvamento
output_path = "test_output"
filename = "teste"
mensagem = load_to_excel(df, output_path, filename)

# Verificar resultado
assert mensagem == "arquivo xlsx salvo com sucesso"
assert os.path.exists(os.path.join(output_path, f"{filename}.xlsx"))
print("✅ Teste manual passou!")

# Limpeza
import shutil
shutil.rmtree(output_path)
```

---

## 📁 Estrutura de Saída

### 🗂️ **Organização Recomendada**
```
data/
└── output/
    ├── 📊 dados_concatenados.xlsx    # Saída padrão
    ├── 📈 relatorio_2024.xlsx        # Relatórios
    ├── 🗓️ backup_20241016.xlsx       # Backups
    └── 📋 logs_processamento.xlsx    # Logs
```

### 🏷️ **Convenções de Nomenclatura**
```python
# Timestamps
filename = f"dados_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

# Identificadores
filename = f"etl_resultado_{run_id}"

# Versionamento
filename = f"dados_v{version_number}"
```

---

## 🔗 Próximos Passos

- 🎯 **Main**: [🎯 Main](main.md) - Orquestração completa
- ⚙️ **Transform**: [⚙️ Transform](transform.md) - Estágio anterior
- 📥 **Extract**: [📥 Extract](extract.md) - Primeiro estágio
- 📖 **Overview**: [📖 Código](codigo.md) - Visão geral da arquitetura
