# Setup — instalar ferramentas e preparar o ambiente

Esta página mostra passo a passo como configurar sua máquina para rodar este projeto: instalar o Python, Poetry, adicionar ao PATH no Windows e executar `poetry install`. Inclui alternativas e dicas para iniciantes.

## 1. Instalar Python

- Baixe o instalador em https://www.python.org/downloads/ (recomenda-se a versão indicada em `pyproject.toml`, ex.: 3.12.7).
- No instalador do Windows, marque "Add Python to PATH".

## 2. Instalar Poetry

### Windows (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

### macOS / Linux

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Verifique a versão:

```powershell
poetry --version
```

## 3. Adicionar Poetry ao PATH (se necessário)

- O instalador do Poetry geralmente adiciona um script no `PATH`. Se `poetry` não for reconhecido, siga as instruções do instalador para adicionar `~/.local/bin` (Linux/macOS) ou `%USERPROFILE%\AppData\Roaming\Python\Scripts` / use o instalador oficial que já altera o PATH.

## 4. Criar/usar o ambiente com Poetry

- Instalar dependências do projeto:

```powershell
poetry install
```

- Executar o projeto:

```powershell
poetry run python src/main.py
```

- Entrar no shell do Poetry:

```powershell
poetry shell
python src/main.py
```

## 5. Alternativas e notas

- Se preferir, você pode usar `pyenv` (documentado em `pyenv.md`) para gerenciar versões do Python e depois usar `poetry env use <path|version>` para fazer o Poetry usar a versão instalada.
- Se o `poetry install` falhar por falta de compiladores, verifique dependências do sistema (em Linux instale `build-essential`, `libssl-dev`, `zlib1g-dev`, etc.).

---

Página criada: `docs/setup.md`
