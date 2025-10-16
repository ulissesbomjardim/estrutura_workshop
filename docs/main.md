# 🎯 Main — Módulo Principal

Este é o módulo principal que orquestra todo o pipeline ETL do projeto, coordenando a execução das três etapas fundamentais.

---

## 🎯 Visão Geral

O módulo `main.py` é o **ponto de entrada** do pipeline ETL, responsável por:

- 🎼 **Orquestrar** todo o fluxo de dados
- 📥 **Coordenar** a extração de dados
- ⚙️ **Gerenciar** a transformação
- 📤 **Controlar** o carregamento
- 📊 **Monitorar** o progresso

---

## 🔧 Funcionalidades

### ✅ **Capacidades**:
- 🎼 Orquestração completa do pipeline
- 📋 Configuração centralizadas de caminhos
- 📊 Monitoramento de tipos de dados
- ✅ Feedback visual do progresso

### ⚡ **Performance**:
- 🚀 Execução sequencial otimizada
- 💾 Gestão eficiente de memória
- 🔄 Processamento em lote

---

## 📖 Documentação da API

### 🎯 **Função Principal**

::: src.main.main

---

## 💻 Código Fonte Completo

```python
from pipeline.extract import extract_from_excel
from pipeline.load import load_to_excel
from pipeline.transform import transform_data


def main() -> None:
    input_path = "data/input"
    output_path = "data/output"
    filename = "dados_concatenados"

    data_list = extract_from_excel(input_path)
    print(type(data_list))

    data_frame = transform_data(data_list)
    print(type(data_frame))

    message = load_to_excel(data_frame, output_path, filename)
    print(message)


if __name__ == "__main__":
    main()
```

---

## 🔄 Fluxo de Execução

```mermaid
graph LR
    A[🚀 Iniciar] --> B[📁 Configurar Caminhos]
    B --> C[📥 Extract]
    C --> D[📊 Verificar Tipos]
    D --> E[⚙️ Transform]
    E --> F[📊 Verificar Tipos]
    F --> G[📤 Load]
    G --> H[✅ Confirmar Sucesso]
    H --> I[🏁 Finalizar]

    style A fill:#e3f2fd
    style C fill:#f3e5f5
    style E fill:#fff3e0
    style G fill:#e8f5e8
    style I fill:#e8f5e8
```

---

## ⚙️ Configuração e Parâmetros

### 📁 **Caminhos de Dados**
```python
# Configurações centralizadas
input_path = "data/input"      # 📥 Dados de entrada
output_path = "data/output"    # 📤 Dados de saída
filename = "dados_concatenados" # 🏷️ Nome do arquivo final
```

### 🔧 **Personalização**
```python
def main_customized(input_dir: str = "data/input",
                   output_dir: str = "data/output",
                   output_name: str = "resultado") -> None:
    """Versão customizável da função main"""

    print(f"📥 Extraindo de: {input_dir}")
    data_list = extract_from_excel(input_dir)
    print(f"✅ Extraídos {len(data_list)} arquivos")

    print(f"⚙️ Transformando dados...")
    data_frame = transform_data(data_list)
    print(f"✅ Dados consolidados: {data_frame.shape}")

    print(f"📤 Salvando em: {output_dir}/{output_name}.xlsx")
    message = load_to_excel(data_frame, output_dir, output_name)
    print(f"✅ {message}")
```

---

## 📊 Monitoramento e Debug

### 🔍 **Informações de Debug**
```python
def main_verbose() -> None:
    """Versão com informações detalhadas"""

    input_path = "data/input"
    output_path = "data/output"
    filename = "dados_concatenados"

    print("🚀 Iniciando pipeline ETL...")

    # Extract
    print("📥 Fase 1: Extração")
    data_list = extract_from_excel(input_path)
    print(f"   📊 Tipo: {type(data_list)}")
    print(f"   📋 Arquivos: {len(data_list)}")
    for i, df in enumerate(data_list):
        print(f"   📄 Arquivo {i+1}: {df.shape}")

    # Transform
    print("⚙️ Fase 2: Transformação")
    data_frame = transform_data(data_list)
    print(f"   📊 Tipo: {type(data_frame)}")
    print(f"   📐 Shape: {data_frame.shape}")
    print(f"   🏷️ Colunas: {list(data_frame.columns)}")

    # Load
    print("📤 Fase 3: Carregamento")
    message = load_to_excel(data_frame, output_path, filename)
    print(f"   ✅ {message}")

    print("🏁 Pipeline concluído com sucesso!")
```

### 📈 **Métricas de Performance**
```python
import time
from typing import Dict, Any

def main_with_metrics() -> Dict[str, Any]:
    """Versão com métricas de performance"""

    metrics = {}
    start_time = time.time()

    input_path = "data/input"
    output_path = "data/output"
    filename = "dados_concatenados"

    # Extract
    extract_start = time.time()
    data_list = extract_from_excel(input_path)
    extract_time = time.time() - extract_start
    metrics['extract_time'] = extract_time
    metrics['files_processed'] = len(data_list)

    # Transform
    transform_start = time.time()
    data_frame = transform_data(data_list)
    transform_time = time.time() - transform_start
    metrics['transform_time'] = transform_time
    metrics['final_rows'] = len(data_frame)
    metrics['final_columns'] = len(data_frame.columns)

    # Load
    load_start = time.time()
    message = load_to_excel(data_frame, output_path, filename)
    load_time = time.time() - load_start
    metrics['load_time'] = load_time

    # Total
    total_time = time.time() - start_time
    metrics['total_time'] = total_time

    print("📊 Métricas de Performance:")
    print(f"   📥 Extração: {extract_time:.2f}s")
    print(f"   ⚙️ Transformação: {transform_time:.2f}s")
    print(f"   📤 Carregamento: {load_time:.2f}s")
    print(f"   🕐 Total: {total_time:.2f}s")

    return metrics
```

---

## 🛠️ Tratamento de Erros

### 🔧 **Versão Robusta**
```python
def main_robust() -> bool:
    """Versão com tratamento de erros"""

    try:
        input_path = "data/input"
        output_path = "data/output"
        filename = "dados_concatenados"

        # Extract
        print("📥 Extraindo dados...")
        data_list = extract_from_excel(input_path)

        if not data_list:
            print("❌ Nenhum arquivo encontrado para processar")
            return False

        print(f"✅ {len(data_list)} arquivos extraídos")

        # Transform
        print("⚙️ Transformando dados...")
        data_frame = transform_data(data_list)
        print(f"✅ Dados consolidados: {data_frame.shape}")

        # Load
        print("📤 Salvando resultado...")
        message = load_to_excel(data_frame, output_path, filename)
        print(f"✅ {message}")

        return True

    except FileNotFoundError as e:
        print(f"❌ Arquivo não encontrado: {e}")
        return False
    except ValueError as e:
        print(f"❌ Erro de dados: {e}")
        return False
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return False
```

---

## 🚀 Formas de Execução

### ⚡ **Execução Padrão**
```bash
# Via Poetry (recomendado)
poetry run python src/main.py

# Via task
poetry run task run

# Com shell ativo
poetry shell
python src/main.py
```

### 🔧 **Execução Customizada**
```python
# Em um script ou notebook
from src.main import main

# Execução normal
main()

# Ou importar e executar partes
from src.pipeline.extract import extract_from_excel
from src.pipeline.transform import transform_data
from src.pipeline.load import load_to_excel

# Execução manual das etapas
data_list = extract_from_excel("data/input")
df = transform_data(data_list)
load_to_excel(df, "data/output", "meu_resultado")
```

---

## 📊 Saída Esperada

### ✅ **Execução Bem-sucedida**
```
<class 'list'>
<class 'pandas.core.frame.DataFrame'>
arquivo xlsx salvo com sucesso
```

### 📋 **Interpretação**
- **Linha 1**: Confirma que `extract_from_excel` retorna uma lista
- **Linha 2**: Confirma que `transform_data` retorna um DataFrame
- **Linha 3**: Confirma que `load_to_excel` salvou com sucesso

---

## 🧪 Testes

### 📋 **Testes Incluídos**
- ✅ Execução completa do pipeline via `runpy`
- ✅ Verificação de chamadas de função com mocks
- ✅ Validação de saída impressa
- ✅ Teste de integração end-to-end

### 🔧 **Executar Testes**
```bash
# Testes específicos do main
poetry run pytest tests/test_pipeline.py -v

# Teste de integração
poetry run pytest tests/test_pipeline.py::test_main_integration -v
```

---

## 🔄 Extensões Possíveis

### 📊 **Logging**
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main_with_logging() -> None:
    """Versão com logging estruturado"""

    logger.info("Iniciando pipeline ETL")

    # Extract
    logger.info("Fase: Extração")
    data_list = extract_from_excel("data/input")
    logger.info(f"Extraídos {len(data_list)} arquivos")

    # Transform
    logger.info("Fase: Transformação")
    data_frame = transform_data(data_list)
    logger.info(f"Dados consolidados: {data_frame.shape}")

    # Load
    logger.info("Fase: Carregamento")
    message = load_to_excel(data_frame, "data/output", "dados_concatenados")
    logger.info(f"Resultado: {message}")

    logger.info("Pipeline concluído")
```

### 🔧 **Configuração Externa**
```python
import json
from pathlib import Path

def main_with_config(config_path: str = "config.json") -> None:
    """Versão com arquivo de configuração"""

    # Carregar configuração
    if Path(config_path).exists():
        with open(config_path, 'r') as f:
            config = json.load(f)
    else:
        config = {
            "input_path": "data/input",
            "output_path": "data/output",
            "filename": "dados_concatenados"
        }

    # Executar pipeline
    data_list = extract_from_excel(config["input_path"])
    data_frame = transform_data(data_list)
    message = load_to_excel(
        data_frame,
        config["output_path"],
        config["filename"]
    )

    print(f"✅ Pipeline executado: {message}")
```

---

## 🔗 Próximos Passos

- 📥 **Extract**: [📥 Extract](extract.md) - Primeiro estágio do pipeline
- ⚙️ **Transform**: [⚙️ Transform](transform.md) - Segundo estágio
- 📤 **Load**: [📤 Load](load.md) - Terceiro estágio
- 📖 **Overview**: [📖 Código](codigo.md) - Visão geral da arquitetura
