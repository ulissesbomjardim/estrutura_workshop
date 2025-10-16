# 🚀 Pipeline — Execução do Projeto ETL

Esta página mostra como executar o pipeline ETL do projeto, desde a preparação dos dados até a verificação dos resultados.

---

## 📊 Visão Geral do Pipeline

```mermaid
graph LR
    A[📥 Arquivos Excel] --> B[🔄 Extract]
    B --> C[⚙️ Transform]
    C --> D[📤 Load]
    D --> E[📋 Resultado Final]

    style A fill:#e1f5fe
    style B fill:#f3e5f5
    style C fill:#e8f5e8
    style D fill:#fff3e0
    style E fill:#fce4ec
```

### 🎯 Fluxo do Processo:
1. **📥 Extract**: Lê arquivos `.xlsx` de `data/input/`
2. **⚙️ Transform**: Concatena todos os DataFrames
3. **📤 Load**: Salva resultado em `data/output/dados_concatenados.xlsx`

---

## 🚀 Como Executar

### ⚡ Execução Rápida (Recomendada)

```bash
# Usando task do Poetry
poetry run task run
```

### 🔧 Execução Manual

```bash
# Opção 1: Via Poetry (sem ativar shell)
poetry run python src/main.py

# Opção 2: Ativando o shell do Poetry
poetry shell
python src/main.py
```

---

## 📁 Preparação dos Dados

### 📋 Requisitos:
- ✅ Arquivos Excel (`.xlsx`) na pasta `data/input/`
- ✅ Mesmo esquema de colunas em todos os arquivos
- ✅ Ambiente Python configurado com Poetry

### 🗂️ Estrutura de Arquivos:
```
projeto/
├── data/
│   ├── input/           # 📥 Coloque seus arquivos .xlsx aqui
│   │   ├── arquivo1.xlsx
│   │   ├── arquivo2.xlsx
│   │   └── ...
│   └── output/          # 📤 Resultado será gerado aqui
│       └── dados_concatenados.xlsx
└── src/
    └── main.py         # 🎯 Script principal
```

---

## ✅ Verificação dos Resultados

### 🔍 Durante a Execução:
O script mostra informações sobre o processamento:

```bash
<class 'list'>                    # Lista de DataFrames extraídos
<class 'pandas.core.frame.DataFrame'>  # DataFrame concatenado
arquivo xlsx salvo com sucesso    # Confirmação de salvamento
```

### 📊 Arquivo de Saída:
- **Local**: `data/output/dados_concatenados.xlsx`
- **Conteúdo**: Todos os dados dos arquivos de entrada concatenados
- **Formato**: Excel sem índices (linhas numeradas automaticamente)

---

## 🛠️ Solução de Problemas

### ❌ Erro: "No such file or directory"
**Causa**: Pasta `data/input/` não existe ou está vazia
**Solução**:
```bash
mkdir -p data/input
# Adicione arquivos .xlsx na pasta
```

### ❌ Erro: "No module named 'openpyxl'"
**Causa**: Dependência para Excel não instalada
**Solução**:
```bash
poetry install
```

### ❌ Erro: "Permission denied" no Windows
**Causa**: Arquivo de saída aberto no Excel
**Solução**: Feche o arquivo Excel e execute novamente

---

## 📖 Documentação Técnica

Para informações detalhadas sobre o código e funções:

- [📖 Overview do Código](codigo.md) - Arquitetura geral
- [🎯 Main](main.md) - Função principal
- [📥 Extract](extract.md) - Módulo de extração
- [⚙️ Transform](transform.md) - Módulo de transformação
- [📤 Load](load.md) - Módulo de carregamento

---

*Para dúvidas sobre configuração inicial, consulte [⚙️ Setup](setup.md)*
