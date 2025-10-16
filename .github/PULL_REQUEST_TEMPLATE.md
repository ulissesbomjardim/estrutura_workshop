Title: tipo(scope): breve descrição — ex: `feat(transform): normaliza colunas de data`

Descrição:

Breve descrição do que este PR faz e por quê.

Motivação / contexto:

Explique o motivo da mudança e qualquer contexto relevante.

Como testar / passos para reproduzir:

1. Criar venv e instalar dependências (poetry install ou pip)
2. Rodar os testes relacionados, por exemplo:

   ```powershell
   python -m pytest tests/test_transform.py
   ```

Checklist:

- [ ] Rodei os testes locais (pytest)
- [ ] Formatei com Black / isort (pre-commit)
- [ ] Adicionei/atualizei testes quando necessário
- [ ] Atualizei a documentação se necessário

Exemplo mínimo:

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
