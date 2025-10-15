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
Git — comandos rápidos (PowerShell)
---------------------------------

Use estes comandos como referência ao trabalhar com branches locais e remotas.

Criar uma branch de feature e enviar para o remoto:

```powershell
git checkout -b feature/minha-feature
git add .
git commit -m "feat: pequena descrição da feature"
git push -u origin feature/minha-feature
```

Atualizar sua branch com as mudanças de `dev` (rebase recomendado para um histórico limpo):

```powershell
git fetch origin
git checkout dev
git pull origin dev
git checkout feature/minha-feature
git rebase origin/dev
# resolver conflitos se houver, depois:
git add .
git rebase --continue
git push --force-with-lease
```

```

```powershell
gh pr create --base dev --head feature/minha-feature --title "feat: resumo" --body "Descrição detalhada do que muda"
```

Branch protection — recomendações rápidas
----------------------------------------

Recomenda-se proteger `main` (e opcionalmente `dev`) com as seguintes regras via GitHub → Settings → Branches → Branch protection rules:

- Branch name pattern: `main`
- Require pull request reviews before merging (1 ou 2 reviewers)
- Require status checks to pass before merging — selecione o workflow de CI (por exemplo: `CI`) e qualquer job crítico
- Include administrators? (opcional) — escolha conforme necessidade organizacional
- Do not allow force pushes
- Require linear history (opcional)
- Enforce code owners (opcional)

Observação importante sobre automações que atualizam branches (ex.: workflow que atualiza `dev` ou cria PRs):

- Nas Settings → Actions → General, configure "Workflow permissions" para "Read and write permissions" para permitir que GitHub Actions faça pushes/atualizações quando necessário.
- Alternativa mais restrita: gerar um Personal Access Token (PAT) com permissões repo:status, repo (push) e salvar como `ACTIONS_PUSH_TOKEN` no Secrets; então usar esse token nos workflows ao invés do token do runner.

Modelo de Pull Request (exemplo)
-------------------------------

Use este modelo como base ao abrir PRs (pode também ser colocado em `.github/PULL_REQUEST_TEMPLATE.md`):

Title: tipo(scope): breve descrição — ex: `feat(transform): normaliza colunas de data`

Body:

- Descrição curta do que o PR faz
- Motivação / contexto
- Como testar / passos para reproduzir
- Checklist:
	- [ ] Rodei os testes locais (pytest)
	- [ ] Formatei com Black / isort (pre-commit)
	- [ ] Adicionei/atualizei testes quando necessário

Exemplo mínimo:

````markdown
Title: feat(transform): normaliza colunas de data

Descrição:

Este PR adiciona a normalização das colunas de data no passo de transformação para evitar erros de parsing.

Como testar:

1. Criar venv e instalar deps
2. Rodar `pytest tests/test_transform.py`

Checklist:

- [x] Testes locais passando
- [x] Código formatado
- [ ] Documentação atualizada
````


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
\n# test trigger\nUpdated: 2025-10-15T10:55:57.4173356-03:00
