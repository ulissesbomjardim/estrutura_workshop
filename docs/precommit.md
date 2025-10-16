# Pre-commit — como funciona e como usar neste projeto

Esta página explica o arquivo `.pre-commit-config.yaml` do projeto, o que cada hook faz, como testar hooks localmente, como configurar o pre-commit para trabalhar com Poetry e como usar as tasks definidas em `pyproject.toml` (format, test, run).

---

## Índice

- O que é pre-commit?
- Analisando `.pre-commit-config.yaml` deste projeto
- O que faz cada hook (black, isort, end-of-file-fixer, trailing-whitespace)
- Como instalar e ativar o pre-commit (com Poetry)
- Como rodar os hooks manualmente (antes do commit)
- Como validar se o commit será aceito (testar hooks localmente)
- O que é o `black` e por que usamos no pre-commit
- Como formatar o código com `isort` + `black`
- Como ativar o venv do Poetry e rodar `task format`, `task test` e `task run`
- Dicas e problemas comuns

---

## O que é pre-commit?

`pre-commit` é uma ferramenta que facilita executar verificações (linters, formatadores, testes rápidos) antes que um commit seja criado. Isso garante que o código que entra no repositório siga padrões comuns (formatação, ordens de imports, remoção de espaços finais, etc.).

Quando configurado, o `pre-commit` instala ganchos (hooks) no Git que são executados automaticamente antes de um `git commit`.

---

## Analisando `.pre-commit-config.yaml` deste projeto

O conteúdo do arquivo no projeto é:

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 25.9.0
    hooks:
      - id: black
        language_version: python3.12

  - repo: https://github.com/PyCQA/isort
    rev: 5.12.0
    hooks:
      - id: isort
        name: isort
        language_version: python3.12

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: end-of-file-fixer
      - id: trailing-whitespace
```

Resumidamente, estamos usando 4 hooks principais:

- `black` (formatador de código)
- `isort` (organizador de imports)
- `end-of-file-fixer` (insere nova linha final se estiver faltando)
- `trailing-whitespace` (remove espaços no final das linhas)

A opção `language_version` indica qual versão do Python usar para rodar o hook (aqui, `python3.12`).

---

## O que faz cada hook

- black: formata automaticamente o código Python conforme regras do projeto (`target-version` e `line-length` configuradas em `pyproject.toml`).
- isort: ordena e agrupa import statements de maneira consistente (ex.: imports padrão, de terceiros e locais separados por linhas vazias).
- end-of-file-fixer: garante que os arquivos terminem com uma nova linha (LF).
- trailing-whitespace: remove espaços desnecessários ao final das linhas.

Esses hooks juntos garantem que o código entregue siga um estilo comum e evite erros de formatação.

---

## Como instalar e ativar o pre-commit (com Poetry)

1. Instale pre-commit (como dependência de desenvolvimento) — se não estiver no `pyproject.toml`:

```powershell
poetry add --dev pre-commit
```

2. Instale os hooks localmente (apenas precisa ser feito uma vez por clone):

```powershell
poetry run pre-commit install
```

Isso criará um hook Git na pasta `.git/hooks/pre-commit` que executa os verificadores antes do commit.

---

## Como rodar os hooks manualmente (antes do commit)

Você pode rodar todos os hooks contra todos os arquivos (útil em CI ou para verificar tudo):

```powershell
poetry run pre-commit run --all-files
```

Ou rodar apenas um hook específico:

```powershell
poetry run pre-commit run black --all-files
```

Se algum hook fizer correção automática (black, isort), ele modificará os arquivos. Depois de alterações, volte a adicionar/commitar os arquivos:

```powershell
git add .
git commit -m "Formata código"
```

---

## Como validar se o commit vai ser aceito (testar hooks localmente)

Use `pre-commit run --all-files` para verificar todos os arquivos. Se todos passarem, o commit é provável que funcione.

No fluxo normal, o pre-commit será executado automaticamente ao rodar `git commit`. Se algum hook falhar (ex.: black alterou arquivos), o commit será abortado e você deverá revisar/adicionar/commit novamente.

---

## O que é o `black` e por que usamos no pre-commit

`black` é um formatador de código opinativo. Ele aplica um estilo consistente automaticamente, evitando discussões sobre formatação. Usamos no pre-commit para garantir que todo o código no repositório esteja formatado automaticamente e de maneira consistente.

No `pyproject.toml` há uma seção `[tool.black]` com `line-length = 88` e `target-version = ["py312"]` — o pre-commit usa essas configurações.

---

## Como formatar o código com `isort` + `black`

O projeto já possui uma task (Taskipy) chamada `format` em `pyproject.toml`:

```toml
[tool.taskipy.tasks]
format = "isort . && black ."
```

Para executar a task format com Poetry, você pode:

```powershell
poetry run task format
# ou
poetry run taskipy format
```

Se você prefere ativar o shell do Poetry e executar direto:

```powershell
poetry shell
poetry run task format
```

---

## Como ativar o venv do Poetry e rodar `task format`, `task test` e `task run`

1. Ativar shell do Poetry (mantém o ambiente ativo):

```powershell
cd G:\dev\Jornada_de_dados\estrutura_workshop
poetry shell
```

2. Rodar tasks definidas em `pyproject.toml`:

```powershell
# format: isort + black
poetry run task format

# test: pytest com cobertura
poetry run task test

# run: executa o script principal
poetry run task run
```

Observação: em alguns setups a task runner pode ser `task` (Taskipy) ou `taskipy`. Se `poetry run task` não funcionar, tente `poetry run taskipy format`.

---

## Dicas e problemas comuns

- Se `pre-commit` reclamar de `black`/`isort` não encontrados, instale `pre-commit` e hooks nas dependências de desenvolvimento do projeto e rode `pre-commit install`.
- Caso `poetry run task format` falhe, verifique se `taskipy` está disponível (instale como dependência dev se necessário).
- Para aplicar as correções do black automaticamente em todos os arquivos, rode `poetry run pre-commit run black --all-files`.

---

Página criada: `docs/precommit.md` — revise e me diga se quer mais exemplos ou imagens.
