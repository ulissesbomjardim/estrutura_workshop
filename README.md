[![Codecov](https://img.shields.io/badge/coverage-unknown-lightgrey)](https://codecov.io/gh/ulissesbomjardim/estrutura_workshop)

# Documentação

A documentação do projeto está publicada em:

- https://ulissesbomjardim.github.io/estrutura_workshop/

# Estrutura Workshop — Jornada de Dados

Material do workshop "Jornada de Dados" — exemplos simples de um pipeline ETL em Python usando pandas.

Resumo rápido
--------------

- Projeto: simples ETL que lê planilhas Excel, concatena em um único DataFrame e salva o resultado.
- Linguagem: Python
- Gerenciador de dependências: Poetry

Requisitos
----------

- Python 3.12 (projeto declara "requires-python = \"3.12.7\"")
- Poetry instalado (para criar/gerenciar o ambiente virtual e dependências)

Instalação e ativação do ambiente (PowerShell)
--------------------------------------------------

1. Instalar dependências e criar ambiente virtual com Poetry:

```powershell
poetry install
```

2. Descobrir o path do venv gerenciado pelo Poetry (opcional):

```powershell
poetry env info --path
```

3. Ativar o venv (exemplo local):

```powershell
& 'G:\dev\Jornada_de_dados\estrutura_workshop\.venv\Scripts\Activate.ps1'
```

Executar o projeto
------------------

O entrypoint de exemplo está em `src/main.py`. Para executar via Poetry sem ativar o shell:

```powershell
poetry run python src/main.py
```

Ou após ativar o ambiente:

```powershell
python src/main.py
```

Comportamento esperado: o script irá procurar arquivos `.xlsx` em `data/input`, concatená-los e salvar o resultado em `data/output/dados_concatenados.xlsx`.

Testes
------

Este projeto usa `pytest`. Os testes estão em `tests/`.

Rodar todos os testes:

```powershell
poetry run pytest -q
```

Rodar testes com coverage (pytest-cov está configurado nas dependências de dev no pyproject):

```powershell
poetry run pytest --cov=src -q
```

Formatação de código
-----------------------

As tasks do `taskipy` (definidas em `[tool.taskipy.tasks]` do `pyproject.toml`) são instaladas no ambiente do Poetry. Execute a task `format` assim:

```powershell
# recomendado: invoke via poetry (não precisa ativar o venv manualmente)
poetry run task format

# alternativa: ative o venv do poetry e rode sem 'poetry run'
$path = poetry env info --path
& "$path\Scripts\Activate.ps1"
task format
```

A task `format` atual chama `isort .`. Para usar também o `black`, atualize a task para `isort . && black .` e garanta que `black` e `isort` estejam instalados no ambiente de desenvolvimento.

Estrutura do repositório
-------------------------

- src/ — código fonte do pacote (package `pipeline`)
  - src/main.py — script de exemplo que executa o pipeline
  - src/pipeline/
    - extract.py — leitura de arquivos .xlsx
    - transform.py — concatena dataframes
    - load.py — salva DataFrame em .xlsx
- data/input — pasta de entrada (xlsx de exemplo)
- data/output — saída gerada pelo pipeline
- tests/ — testes pytest

Git / Pull Requests (dicas rápidas)
------------------------------------

- Criar uma branch de feature e enviar para o remoto:

```powershell
git checkout -b feature/minha-feature
git add .
git commit -m "feat: pequena descrição da feature"
git push -u origin feature/minha-feature
```

- Criar PR com a CLI `gh`:

```powershell
gh pr create --base dev --head feature/minha-feature --title "feat: resumo" --body "Descrição"
```

CI / Codecov
------------

- O repositório inclui integração de CI (GitHub Actions) e upload para Codecov.
- Para repositórios privados, configure o secret `CODECOV_TOKEN` em Settings → Secrets and variables → Actions com o token obtido no site do Codecov.

Updated: 2025-10-15T10:55:57.4173356-03:00
