# Testes — explicação detalhada dos arquivos em `tests/` e como rodá-los

Esta página documenta os testes existentes neste repositório, descreve para que cada teste serve, quais asserts são verificados, como rodar os testes localmente e como interpretar os resultados.

---

## Rodando os testes localmente

Recomendo usar Poetry para garantir que as dependências de teste estejam disponíveis:

```powershell
poetry install
poetry run pytest -q
```

- `-q` reduz a verbosidade. Remova para ver saída completa.
- Para ver cobertura (se instalado/configurado):

```powershell
poetry run pytest --cov=src
```

---

## Estrutura da pasta `tests/`

```
tests/
├─ test_transform.py    # testes para a função transform_data
├─ test_load.py         # testes para a função load_to_excel
└─ test_pipeline.py     # teste de integração/smoke test no script src/main.py
```

Abaixo descrevo cada arquivo de teste.

---

### `tests/test_transform.py`

Objetivo
- Verificar o comportamento de `transform_data` (concatenação de DataFrames).

Testes contidos
- `test_concat_two_dataframes`: concatena dois DataFrames com mesmas colunas e compara resultado com `pd.concat`.
- `test_single_dataframe_returns_same_dataframe`: garante que ao passar uma lista com único DataFrame o retorno é igual à concatenação de uma lista com esse mesmo DataFrame.
- `test_empty_list_raises_value_error`: verifica se passar lista vazia lança `ValueError`.
- `test_concat_different_columns_creates_union_and_fills_nan`: testa concatenação quando colunas diferem entre DataFrames (espera união de colunas e preenchimento com NaN onde necessário).

Como os asserts funcionam
- Usa `pandas.DataFrame.equals` para comparar DataFrames que verificam tanto valores quanto posições de colunas/nomes.
- Para o caso com colunas diferentes, o teste compara `list(result.columns)` com `list(expected.columns)` e então `result.equals(expected)` para garantir igualdade estrutural.

Dicas para depuração
- Rode `pytest -k transform -q -vv` para rodar apenas os testes de transform.
- Se a função mudar, atualize os testes para refletir o comportamento desejado (por exemplo, ordenação de colunas).

---

### `tests/test_load.py`

Objetivo
- Validar que `load_to_excel` grava corretamente um DataFrame em `.xlsx`, cria diretórios faltantes e retorna a mensagem esperada.

Testes contidos
- `test_load_to_excel_creates_file_and_returns_message`:
  - Cria um DataFrame de teste, chama `load_to_excel` com `tmp_path/out` e confirma que o arquivo existe e que a mensagem retornada é "arquivo xlsx salvo com sucesso".
  - Lê o arquivo salvo com `pd.read_excel` e usa `pandas.testing.assert_frame_equal` para comparar com o DataFrame original.
- `test_load_to_excel_creates_nested_dir_if_missing`:
  - Usa `tmp_path` para apontar a um diretório que não existe (ex: `tmp_path/nested/dir`) e confirma que a função cria a pasta e salva o arquivo.

Sobre `tmp_path`
- `tmp_path` é uma fixture do pytest que fornece um diretório temporário isolado para o teste. Tudo dentro dele é removido ao final do teste.

Dicas para depuração
- Se o teste falhar ao salvar o arquivo, verifique permissões ou se o `openpyxl` está instalado.
- Se a leitura do Excel retorna diferença, verifique se `df.to_excel` salvou índices ou tipos diferentes; o teste usa `reset_index(drop=True)` ao comparar para evitar diferenças de índice.

---

### `tests/test_pipeline.py`

Objetivo
- Teste de integração leve que verifica se `src/main.py` chama as funções `extract_from_excel`, `transform_data` e `load_to_excel` com os argumentos corretos e imprime mensagens esperadas.

Abordagem do teste
- Usa `monkeypatch` para injetar módulos falsos (`pipeline.extract`, `pipeline.transform`, `pipeline.load`) no `sys.modules` e atribuir funções mock que registram chamadas em um dicionário `called`.
- Executa `runpy.run_path("src/main.py", run_name="__main__")` para rodar o script como se fosse chamado diretamente.
- Verifica que `called` contém chamadas com os parâmetros corretos (`data/input`, `data/output`, `dados_concatenados`) e que a saída impressa (`capsys`) contém as mensagens previstas.

Por que usar mocks aqui?
- Evita dependências de I/O (ler arquivos Excel reais) e torna o teste rápido e determinístico.

Dicas para depuração
- Se o teste falhar, verifique o que foi impresso em `capsys` e se as funções foram chamadas — o dicionário `called` é inspecionado.
- Se a importação falhar, verifique caminhos e se os módulos foram corretamente colocados em `sys.modules`.

---

## Interpretação dos resultados

- `OK`/`PASSED`: todos os testes passaram.
- `FAILED`: um ou mais testes falharam — o pytest mostrará uma stack trace e um resumo indicando quais asserts falharam e em quais linhas.

Comandos úteis

```powershell
# rodar todos os testes
poetry run pytest -q

# rodar testes com saída detalhada
poetry run pytest -vv

# rodar testes de apenas um arquivo
poetry run pytest tests/test_load.py -q

# rodar apenas testes com palavra-chave
poetry run pytest -k load -q
```

---

## Adicionando novos testes

- Use fixtures do pytest (como `tmp_path`) para criar diretórios/arquivos temporários.
- Para testar funções de transformação, crie DataFrames pequenos com `pd.DataFrame`.
- Para testar I/O, prefira `tmp_path` para evitar poluir o repositório com artefatos.

---

Página criada: `docs/tests.md`

Se quiser, eu posso:
- Adicionar `tests.md` ao `mkdocs.yml` nav;
- Gerar exemplos de arquivos Excel usados nos testes e adicionar um script `scripts/generate_test_files.py`;
- Adicionar instruções para executar testes isoladamente no CI (workflow `ci.yml`).
