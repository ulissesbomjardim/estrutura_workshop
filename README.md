[![Codecov](https://img.shields.io/badge/coverage-unknown-lightgrey)](https://codecov.io/gh/ulissesbomjardim/estrutura_workshop)

# Estrutura Workshop

Este repositório contém material do workshop "Jornada de Dados".

Como ativar o ambiente (PowerShell)

1. Descobrir o path do venv gerenciado pelo Poetry:

```powershell
poetry env info --path
```

2. Ativar o venv criado localmente (exemplo para este projeto):

```powershell
& 'G:\dev\Jornada_de_dados\estrutura_workshop\.venv\Scripts\Activate.ps1'
```

Executar comandos sem ativar o shell

```powershell
poetry run python -V
poetry run python script.py
```

Criar/instalar dependências

```powershell
poetry env use python
poetry install
```

Observação sobre 'touch' no PowerShell

- O comando `touch` é um utilitário típico de sistemas Unix (bash). No PowerShell use:

```powershell
# cria o arquivo README.md se não existir
New-Item README.md -ItemType File -Force
```

Ou no cmd.exe:

```bat
copy NUL README.md
```

CI / Codecov
------------

Para que o upload de cobertura funcione em repositórios privados no GitHub Actions, adicione o secret `CODECOV_TOKEN` nas configurações do repositório:

1. No GitHub, abra o repositório > Settings > Secrets and variables > Actions.
2. Clique em "New repository secret".
3. Nomeie como `CODECOV_TOKEN` e cole o token que você obteve do Codecov (Settings > Tokens no site do Codecov).
4. Salve.

Se o repositório for público, o upload normalmente funciona sem token, mas adicionar o secret permite garantir controle sobre o upload.

Observação sobre caching
------------------------

O workflow do CI já tenta acelerar execuções usando cache. Se quiser ajustar o cache (por exemplo, incluir virtualenvs), edite `.github/workflows/ci.yml`.

CI trigger
----------

Este arquivo foi atualizado para forçar uma nova execução do workflow de CI para validação em 2025-10-15.

Codecov: como obter o token e configurar (rápido)
-----------------------------------------------

Onde obter o token:

- Acesse https://codecov.io e autentique com a conta ligada ao seu GitHub.
- Abra o repositório correspondente no Codecov.
- Vá em Settings / Repository Upload Token (ou similar) e copie o token.

Como adicionar o token no GitHub (web UI):

1. No GitHub abra o repositório → Settings → Secrets and variables → Actions.
2. Clique em "New repository secret".
3. Name: `CODECOV_TOKEN`  — Value: cole o token do Codecov.
4. Salve.

Como adicionar o token com a CLI `gh` (PowerShell):

```powershell
# login se necessário
gh auth login

# definir secret (modo simples)
gh secret set CODECOV_TOKEN --body '<COLE_AQUI_O_TOKEN>' --repo ulissesbomjardim/estrutura_workshop
```

Depois disso, re-run o workflow e verifique a etapa "Upload coverage to Codecov" para garantir que o upload foi bem sucedido.
