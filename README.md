[![Codecov](https://img.shields.io/badge/coverage-unknown-lightgrey)](https://codecov.io/gh/ulissesbomjardim/estrutura_workshop)

# test trigger
Updated: 2025-10-15T10:55:57.4173356-03:00
<!-- debug: test PR creation -->
[![Codecov](https://img.shields.io/badge/coverage-unknown-lightgrey)](https://codecov.io/gh/ulissesbomjardim/estrutura_workshop)

# Estrutura Workshop

[![Codecov](https://codecov.io/gh/ulissesbomjardim/estrutura_workshop/branch/main/graph/badge.svg)](https://codecov.io/gh/ulissesbomjardim/estrutura_workshop)

# Estrutura Workshop

> Material do workshop "Jornada de Dados" — scripts e pipelines de exemplo para extração, transformação e carga.

## Quickstart (PowerShell)

1. Instale dependências e crie/ative o ambiente (Poetry):

```powershell
poetry env use python
poetry install
poetry env info --path
& '<repo>\\.venv\\Scripts\\Activate.ps1'
```

Substitua `<repo>` pelo caminho do projeto local, por exemplo `G:\dev\Jornada_de_dados\estrutura_workshop`.

## Git / fluxo de trabalho

Criar uma branch de feature e enviar para o remoto:

```powershell
git checkout -b feature/minha-feature
git add .
git commit -m "feat: descrição curta"
git push -u origin feature/minha-feature
```

Criar PR (exemplo com `gh`):

```powershell
gh pr create --base dev --head feature/minha-feature --title "feat: resumo" --body "Descrição do que muda"
```

Recomenda-se usar `dev` como integração e `main` como release estável. O repositório possui workflows que automatizam PRs e approvals.

## Modelo de Pull Request (resumido)

- Title: tipo(scope): breve descrição — ex: `feat(transform): normaliza datas`
- Body: curta descrição, motivação, passos para testar
- Checklist:
  - [ ] Rodei os testes locais (pytest)
  - [ ] Formatei com Black / isort
  - [ ] Adicionei/atualizei testes quando necessário

## Branch protection (recomendado)

Proteja `main` com regras como: exigir revisões, checks obrigatórios e proibir force-push.

## CI / Codecov

- O workflow `CI` roda em pushes para `main` e `dev` e em PRs.
- Para upload de cobertura em repositórios privados adicione o secret `CODECOV_TOKEN` (Settings → Secrets → Actions).

## Como o fluxo automático funciona aqui

- Push em `feature/**` → executa `push-create-pr.yml` que roda testes, cria/atualiza PR para `dev` e abre uma issue pedindo aprovação.
- Comentário `/approve-pr #NN` em uma issue por um mantenedor aciona `approve-pr.yml` que faz squash-merge do PR para `dev` (usando `ACTIONS_PUSH_TOKEN` se disponível).
- Quando uma PR para `dev` é *mesclada* (merged), o workflow `create-pr-dev-to-main.yml` cria/atualiza automaticamente uma PR de `dev` → `main` para revisão final.

## Observações

- Se quiser que eu deixe o PR criado para `main` como draft automaticamente, ou adicionar reviewers/labels, eu implemento.
- Se preferir dividir a documentação em `docs/`, também posso mover e gerar um índice.
