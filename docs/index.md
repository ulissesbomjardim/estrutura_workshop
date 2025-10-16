# Estrutura Workshop — Documentação principal

Bem-vindo à documentação do projeto "Estrutura Workshop". Use este índice para navegar rapidamente entre os guias específicos (Setup, Pipeline, Tests, CI, Pyenv, Pre-commit e Git).

## Navegação rápida

- Setup: passos para instalar Python e Poetry, configurar PATH no Windows e rodar `poetry install`. (veja `setup.md`)
- Pipeline: visão detalhada do ETL (extract, transform, load) e como executar as funções. (veja `pipeline.md`)
- Tests: como os testes estão organizados, como rodá-los e interpretar resultados. (veja `tests.md`)
- CI: descrição dos workflows do GitHub Actions usados no repositório. (veja `ci.md`)
- pyenv: como gerenciar versões do Python com `pyenv`/`pyenv-win`. (veja `pyenv.md`)
- Pre-commit: configuração dos hooks (black, isort) e como usá-los. (veja `precommit.md`)
- Git: explicações sobre `.git`, `.github`, `.gitattributes`, `.gitignore`, criar repositório e tokens. (veja `git.md`)

## Passos rápidos para começar (resumido)

1. Clonar o repositório:

```powershell
git clone <URL-DO-REPO>
cd estrutura_workshop
```

2. Instalar dependências com Poetry:

```powershell
poetry install
```

3. Rodar testes:

```powershell
poetry run pytest -q
```

4. Rodar o pipeline de exemplo:

```powershell
poetry run python src/main.py
```

5. Rodar a documentação localmente com MkDocs:

```powershell
poetry run mkdocs serve
```

## Resumo e links

Veja as páginas específicas para guias passo a passo e explicações completas:

- Setup: `setup.md`
- Pipeline: `pipeline.md`
- Tests: `tests.md`
- CI: `ci.md`
- pyenv: `pyenv.md`
- Pre-commit: `precommit.md`
- Git: `git.md`

Se algo não estiver funcionando localmente (por exemplo `mkdocs serve` retornando erro), cole a saída do terminal aqui que eu ajudo a diagnosticar.

---

Documentação atualizada.
Instalação e uso (passos):
