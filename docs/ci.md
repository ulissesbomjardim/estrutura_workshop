# CI — descrição dos workflows do GitHub Actions

Esta página explica detalhadamente os workflows existentes em `.github/workflows/` e como eles funcionam neste repositório.

## Workflows presentes

1. `ci.yml` — pipeline principal de CI (testes, checagem de style e upload de cobertura)
2. `push-create-pr.yml` — executa testes em branches `feature/**` e `test/**` e cria/atualiza PRs para `dev`
3. `create-pr-dev-to-main.yml` — roda testes em PRs para `dev` e cria PR `dev -> main` quando `dev` for merged

### `ci.yml` (detalhes)

- Eventos: `push` e `pull_request` para branches `main` e `dev`.
- Permissões: `contents: read`, `pull-requests: write`.
- Jobs:
  - `test`:
    - `runs-on: ubuntu-latest`.
    - Usa `actions/checkout@v4` com token `${{ secrets.ACTIONS_PUSH_TOKEN }}`.
    - `actions/setup-python@v4` com `python-version: 3.12`.
    - Instala dependências (pip): pandas, openpyxl, pytest, pytest-cov, black, isort, codecov.
    - Roda `black --check` para checar formatação.
    - Roda `pytest` com cobertura e gera `coverage.xml`.
    - Se `CODECOV_TOKEN` estiver definido, faz upload para Codecov.

Notas de configuração:
- Crie `secrets.CODECOV_TOKEN` se quiser que o upload de cobertura seja feito.
- `ACTIONS_PUSH_TOKEN` parece ser usado para checkout com permissões — garanta que ele exista se necessário.

### `push-create-pr.yml` (detalhes)

- Eventos: `push` em branches `feature/**` e `test/**`.
- Jobs:
  - `test`: instala dependências mínimas e roda `pytest`.
  - `create_pr`: cria/atualiza um PR da branch atual para `dev` usando `actions/github-script@v6`.

Permissões necessárias:
- `contents: write`, `pull-requests: write` são necessários para criar PRs. O workflow usa `${{ secrets.GITHUB_TOKEN }}` para autenticar.

### `create-pr-dev-to-main.yml` (detalhes)

- Eventos: PRs envolvendo `dev` (abertos, sincronizados, fechados).
- Jobs:
  - `test-on-pr`: roda testes quando a PR não está fechada.
  - `create-pr-to-main`: se a PR foi merged (`github.event.pull_request.merged == true`), cria PR `dev -> main` automaticamente.

Notas:
- O passo que cria PR tenta ler `.github/PULL_REQUEST_TEMPLATE.md` e usa como corpo do PR.
- Para que a criação de PR funcione ao merge, o workflow precisa de permissão de escrita (`contents: write`, `pull-requests: write`).

---

## Como testar workflows localmente

- Você pode usar a ferramenta `act` (https://github.com/nektos/act) para rodar workflows localmente, mas atenção: `act` tem limitações e pode precisar de imagens Docker específicas.
- Alternativa: crie um branch de teste no GitHub e observe os workflows executando na aba Actions.

## Ajustes comuns para funcionar corretamente

- Configure os secrets necessários em Settings → Secrets and variables → Actions:
  - `CODECOV_TOKEN` (opcional)
  - `ACTIONS_PUSH_TOKEN` (se usado)
- Verifique `permissions` no topo dos workflows; se o workflow precisa gravar (ex.: criar PRs) garanta `contents: write` e `pull-requests: write`.

---

Página criada: `docs/ci.md`
