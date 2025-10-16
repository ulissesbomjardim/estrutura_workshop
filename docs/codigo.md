# Documentação do Código - Pipeline ETL

Esta seção contém a documentação detalhada de todos os módulos Python do projeto.

## Arquitetura do Pipeline

O projeto segue uma arquitetura ETL (Extract, Transform, Load) simples e eficiente:

```mermaid
graph LR
    A[Arquivos Excel] --> B[Extract]
    B --> C[Transform]
    C --> D[Load]
    D --> E[Arquivo Consolidado]
```

## Estrutura dos Módulos

### 📁 src/
- **`main.py`**: Ponto de entrada do pipeline que orquestra todo o processo
- **`pipeline/`**: Pacote contendo os módulos do pipeline ETL

### 📁 src/pipeline/
- **`extract.py`**: Módulo de extração de dados
- **`transform.py`**: Módulo de transformação de dados
- **`load.py`**: Módulo de carregamento de dados

## Fluxo de Execução

1. **Extração**: O módulo `extract` lê todos os arquivos `.xlsx` do diretório `data/input/`
2. **Transformação**: O módulo `transform` concatena todos os DataFrames em um único
3. **Carregamento**: O módulo `load` salva o resultado final em `data/output/`

## Navegação

Use o menu lateral para acessar a documentação detalhada de cada módulo:

- [Main](main.md) - Módulo principal
- [Extract](extract.md) - Extração de dados
- [Transform](transform.md) - Transformação de dados
- [Load](load.md) - Carregamento de dados
