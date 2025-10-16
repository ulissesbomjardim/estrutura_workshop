# Git e GitHub — conceitos, arquivos e CI/CD

Esta página explica em detalhes o que são e para que servem os arquivos/pastas relacionados ao Git e GitHub neste repositório, como criar um repositório no GitHub, como configurar GitHub Actions (CI/CD), como gerar tokens/secrets e os principais comandos Git. Tudo em linguagem acessível para que qualquer pessoa consiga entender e reproduzir.

---

## Índice

- O que é `.git`?
- O que é `.github/` e o que vai dentro dela?
- O que fazem `.gitattributes` e `.gitignore`?
- Como criar esses arquivos/pastas localmente
- Como criar um repositório no GitHub e enviar o projeto
- GitHub Actions: como funcionam, permissões e secrets
- Tokens e Secrets: criar e configurar
- Principais comandos Git (passo a passo)
- Como o CI/CD foi criado neste projeto (análise dos workflows)
- Dicas e problemas comuns

---

## O que é `.git`?

- `.git` é a pasta oculta que o Git cria no diretório do projeto quando você inicializa um repositório com `git init` ou quando clona um repositório (`git clone`).
- Ela contém todo o histórico de versões, referências, branches, tags, objetos (commits, blobs), configuração local e hooks.
- Você normalmente não olha dentro desta pasta nem a comita — ela é o "banco de dados" do Git para o seu repositório local.

Exemplo: se você rodar `git init` na raiz do projeto, será criada a pasta `.git/`.

```powershell
cd G:\dev\Jornada_de_dados\estrutura_workshop
git init
ls -Force -Directory
# verá .git entre os diretórios ocultos
```

---

## O que é `.github/`?

- `.github/` é uma pasta no repositório onde você coloca arquivos específicos do GitHub: templates de Pull Request, templates de issues, workflows do GitHub Actions, e outras configurações (dependabot, CODEOWNERS, etc).
- No nosso projeto existe:
  - `.github/PULL_REQUEST_TEMPLATE.md` — template usado quando alguém abre um pull request.
  - `.github/workflows/` — contém os YAMLs que descrevem pipelines de CI/CD (GitHub Actions).

Arquivos comuns dentro de `.github/`:
- `workflows/*.yml` — pipelines do Actions.
- `DEPENDABOT.yml` — configurações do Dependabot.
- `CODEOWNERS` — define quem é responsável por arquivos/paths.
- `PULL_REQUEST_TEMPLATE.md` / `ISSUE_TEMPLATE/` — templates para PRs e issues.

---

## O que fazem `.gitattributes` e `.gitignore`?

### `.gitattributes`
- Controla como o Git trata arquivos (fins de linha, diff/merge, filtros, linguagens para linguist).
- No projeto temos regras para forçar LFs em arquivos de texto e manter CRLF em scripts PowerShell, além de marcar imagens e binários como `binary`.
- Exemplo de uso prático: evitar que arquivos Markdown ou YAML mudem automaticamente os fins de linha entre plataformas.

### `.gitignore`
- Diz ao Git quais arquivos/pastas não devem ser monitorados pelo versionamento (ex.: `.venv/`, `site/`, `__pycache__/`).
- Evita que arquivos temporários, chaves e builds sejam acidentalmente adicionados ao repositório.

---

## Como criar esses arquivos/pastas localmente

### Criar `.git` (inicializar repositório)

```powershell
cd G:\dev\Jornada_de_dados\estrutura_workshop
git init
```

ou clonar um repositório remoto:

```powershell
git clone https://github.com/<usuario>/<repositorio>.git
```

### Criar `.github/` e workflows

```powershell
mkdir .github
mkdir .github\workflows
# criar arquivo de workflow
notepad .github\workflows\ci.yml
```

### Criar `.gitignore` e `.gitattributes`

Crie os arquivos na raiz e adicione regras, por exemplo:

`.gitignore` (exemplo mínimo):

```
.venv/
__pycache__/
*.pyc
site/
```

`.gitattributes` (exemplo mínimo):

```
*.md text eol=lf
*.py text eol=lf
*.ps1 text eol=crlf
```

Depois adicione e comite:

```powershell
git add .gitignore .gitattributes
git commit -m "Add gitignore and gitattributes"
```

---

## Como criar um repositório no GitHub e enviar o projeto

1. No GitHub, clique em "New repository".
2. Preencha o nome, descrição e escolha público ou privado.
3. Não marque a opção de criar `README`/`.gitignore` se você já tiver esses arquivos localmente (ou marque se preferir).
4. Após criado, GitHub mostra a URL para clonar/push remoto.

Exemplo de fluxo local para enviar:

```powershell
# cria remote chamado origin
git remote add origin https://github.com/<usuario>/<repositorio>.git
# verificar branch atual (ex: main)
git branch -M main
# enviar ao remote
git push -u origin main
```

Se o repositório for privado e for usar SSH, use a URL SSH `git@github.com:usuario/repositorio.git`.

---

## GitHub Actions — como funcionam

- GitHub Actions executa pipelines definidas por arquivos YAML em `.github/workflows/` quando eventos acontecem (push, pull_request, schedule, etc).
- Cada workflow tem *jobs* e cada job tem *steps*. Jobs rodam em *runners* (máquinas virtuais hospedadas pelo GitHub ou self-hosted).
- Workflows podem usar *actions* (reutilizáveis) ou executar comandos diretamente.

Estrutura mínima de um workflow:

```yaml
name: CI
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install poetry
          poetry install
      - name: Run tests
        run: poetry run pytest -q
```

---

## Ajustes necessários para Actions funcionar neste projeto

1. Certifique-se de que os workflows existam em `.github/workflows/` (no projeto já existem: `ci.yml`, `create-pr-dev-to-main.yml`, `push-create-pr.yml`).
2. Se o workflow usar secrets (ex: AWS credentials, token para publicar), crie esses secrets no repositório GitHub:
   - Vá em Settings → Secrets and variables → Actions → New repository secret
   - Nomeie e cole o valor. (Ex: `PYPI_TOKEN`, `GITHUB_TOKEN` geralmente já é provido automaticamente para ações básicas)
3. Se o workflow usar permissões especiais (ex: write access to PRs, actions), ajuste o `permissions` no workflow e em Settings → Actions → General.
4. Se o workflow precisar de um token PAT (Personal Access Token) com escopos extras, crie no GitHub em Settings → Developer settings → Personal access tokens → Tokens (classic) e forneça o token como secret.

---

## Tokens e Secrets — como criar

### Criar um Personal Access Token (PAT)

1. No GitHub (web): Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token.
2. Selecione escopos necessários (por exemplo `repo` para acesso a repositórios privados, `workflow` para acionar workflows, `write:packages` para publicar pacotes).
3. Copie o token gerado (ele aparece apenas uma vez) e adicione como secret no repositório.

### Adicionar secret no repositório

- Vá em Settings → Secrets and variables → Actions → New repository secret
- Nome: `MY_PAT`
- Valor: cole o token

No workflow use o secret assim:

```yaml
- name: Checkout
  uses: actions/checkout@v4
  with:
    token: ${{ secrets.MY_PAT }}
```

---

## Principais comandos Git (passo a passo para iniciantes)

### Configurar seu usuário

```powershell
git config --global user.name "Seu Nome"
git config --global user.email seu.email@example.com
```

### Fluxo comum de trabalho (branchs, commit, push)

```powershell
# criar nova branch
git checkout -b feature/minha-tarefa
# adicionar alterações
git add .
# commitar
git commit -m "Implementa X"
# enviar branch
git push -u origin feature/minha-tarefa
```

### Atualizar branch com main

```powershell
git checkout main
git pull origin main
git checkout feature/minha-tarefa
git merge main
# resolver conflitos se houver
```

### Trabalhar com PRs (GitHub)

- Faça push da branch, abra um Pull Request no GitHub, peça revisão, corrija comentários, faça merge.
- Você pode também criar PRs via CLI (`gh`):

```powershell
gh pr create --base main --head feature/minha-tarefa --title "Minha PR" --body "Descrição"
```

---

## Como o CI/CD foi criado neste projeto (análise dos workflows)

Este projeto inclui três workflows em `.github/workflows/`:

1. `ci.yml` — workflow principal de CI.
2. `push-create-pr.yml` — workflow que pode criar PRs automaticamente em determinados branches.
3. `create-pr-dev-to-main.yml` — workflow que cria PRs de `dev` para `main` (provavelmente usado para automação de release/merge entre branches).

Vou descrever resumidamente cada um (analise simplificada dos arquivos):

### `ci.yml`
- Eventos: executa em `push` e `pull_request`.
- Etapas comuns:
  - Checkout do código (`actions/checkout`).
  - Setup do Python (`actions/setup-python`).
  - Instalar dependências (Poetry) e executar `pytest`.
  - Pode realizar lint, formatação e upload de cobertura.

### `push-create-pr.yml` e `create-pr-dev-to-main.yml`
- Provavelmente usam `peter-evans/create-pull-request` action ou ações customizadas para abrir PRs automaticamente quando certos eventos ocorrem.
- Útil para automatizar sincronização entre branches ou criar PRs de release.

> Observação: Para descrever exatamente o que cada workflow faz, abra os arquivos YAML. Abaixo há um resumo extraído automaticamente.

---

## Exemplo: configurar um workflow básico para este projeto

Arquivo: `.github/workflows/ci.yml` (exemplo simplificado)

```yaml
name: CI
on:
  push:
    branches: [ main, feature/* ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: '3.12'
      - name: Install Poetry
        run: |
          python -m pip install --upgrade pip
          pip install poetry
      - name: Install dependencies
        run: poetry install
      - name: Run tests
        run: poetry run pytest -q
```

---

## Dicas e problemas comuns

- Lembre-se de adicionar secrets via Settings → Secrets.
- Se um workflow precisa criar PRs programaticamente, um PAT com escopo `repo` pode ser necessário.
- `GITHUB_TOKEN` é automaticamente injetado nos workflows; porém seu escopo é limitado — para operações que precisam de permissões extra (por exemplo, publicar em outro repositório), crie um PAT e use como secret.
- Verifique `permissions` no topo do workflow YAML se você precisa de permissões de escrita para actions e tokens.

---

## Conclusão

Esta página explicou o que são os principais arquivos relacionados ao Git/GitHub, como criá-los e como configurar CI/CD com GitHub Actions. Se quiser, eu posso:

- Gerar exemplos visuais (capturas) se você colar saídas do terminal;
- Criar um workflow de exemplo mais completo para este repositório (com lint, teste e publicação);
- Adicionar instruções específicas para configurar `dependabot` ou `CODEOWNERS`.

---

Página criada: `docs/git.md`
