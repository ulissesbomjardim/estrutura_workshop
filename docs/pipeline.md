# Pipeline — documentação da pasta `src` e instruções de uso

Esta página descreve a estrutura da pasta `src/` do projeto, explica o propósito de cada arquivo no pacote `pipeline` e documenta todas as funções públicas com exemplos de uso e instruções para executar o pipeline localmente.

---

## Visão geral da estrutura

```
src/
├─ main.py                # entrypoint do projeto - orquestra o ETL
└─ pipeline/
   ├─ __init__.py         # torna `pipeline` um pacote
   ├─ extract.py          # funções de extração (leitura de .xlsx)
   ├─ transform.py        # funções de transformação (concatenação)
   └─ load.py             # funções de carga (salvar em .xlsx)
```

O pipeline é simples: extract -> transform -> load.

- extract: lê todos os arquivos `*.xlsx` em `data/input/` e retorna uma lista de DataFrames.
- transform: recebe a lista de DataFrames e concatena em um único DataFrame.
- load: grava o DataFrame resultante em `data/output/dados_concatenados.xlsx`.

---

## Arquivos e funções (documentação detalhada)

### `src/main.py`

Propósito
- Ponto de entrada do projeto. Orquestra as etapas do pipeline chamando as funções do pacote `pipeline`.

Conteúdo relevante
```python
from pipeline.extract import extract_from_excel
from pipeline.load import load_to_excel
from pipeline.transform import transform_data


def main() -> None:
    input_path = "data/input"
    output_path = "data/output"
    filename = "dados_concatenados"

    data_list = extract_from_excel(input_path)
    print(type(data_list))

    data_frame = transform_data(data_list)
    print(type(data_frame))

    message = load_to_excel(data_frame, output_path, filename)
    print(message)


if __name__ == "__main__":
    main()
```

Como executar

- Usando Poetry (recomendado):

```powershell
poetry run python src/main.py
```

- Ou ativando o shell do Poetry:

```powershell
poetry shell
python src/main.py
```

O script espera encontrar arquivos `.xlsx` em `data/input/`. Depois de executar, ele criará `data/output/dados_concatenados.xlsx`.

---

### `src/pipeline/extract.py`

Propósito
- Localizar e ler todos os arquivos Excel (`.xlsx`) em um diretório de entrada e retornar uma lista de `pandas.DataFrame`.

Assinatura pública

```python
def extract_from_excel(input_path: str) -> List[pd.DataFrame]
```

Parâmetros
- `input_path` (str): caminho para o diretório que contém arquivos `.xlsx`.

Retorno
- `List[pandas.DataFrame]`: lista de DataFrames, um por arquivo lido.

Comportamento
- Usa `glob` para encontrar `*.xlsx` no diretório especificado.
- Para cada arquivo encontrado chama `pandas.read_excel(file_path)` e adiciona o DataFrame à lista.
- Se nenhum arquivo for encontrado retorna uma lista vazia.

Exemplo de uso

```python
from pipeline.extract import extract_from_excel

lista = extract_from_excel("data/input")
print(len(lista))
for df in lista:
    print(df.shape)
```

Observações / edge cases
- Arquivos com formatos inválidos ou proteções podem causar exceção ao `pandas.read_excel`; trate com `try/except` se desejar robustez extra.
- Se você quiser ler arquivos CSV, extenda a função ou adicione uma nova função `extract_from_csv`.

---

### `src/pipeline/transform.py`

Propósito
- Receber uma lista de `pandas.DataFrame` e concatená-los em um único DataFrame.

Assinatura pública

```python
def transform_data(data_list: list[pd.DataFrame]) -> pd.DataFrame
```

Parâmetros
- `data_list`: lista de `pandas.DataFrame` a serem concatenados.

Retorno
- `pandas.DataFrame`: DataFrame resultante da concatenação.

Exceções
- `ValueError` se `data_list` for vazio (a função exige pelo menos 1 DataFrame).

Implementação (resumida)
- Verifica se `data_list` não está vazio.
- Usa `pd.concat(data_list, ignore_index=True)` para concatenar.

Exemplo de uso

```python
from pipeline.transform import transform_data
import pandas as pd

# exemplo: concatenar duas tabelas
df1 = pd.DataFrame({"a": [1, 2]})
df2 = pd.DataFrame({"a": [3, 4]})
resultado = transform_data([df1, df2])
print(resultado)
```

Observações
- Se os DataFrames tiverem colunas diferentes, `pd.concat` preencherá valores ausentes com `NaN`.
- Validações adicionais (tipos de colunas, limpeza) podem ser feitas antes da concatenação.

---

### `src/pipeline/load.py`

Propósito
- Salvar um `pandas.DataFrame` em um arquivo Excel `.xlsx` em um diretório de saída.

Assinatura pública

```python
def load_to_excel(df: pd.DataFrame, output_path: str, filename: str) -> str
```

Parâmetros
- `df`: DataFrame a ser salvo.
- `output_path`: diretório onde o arquivo será criado (ex: `data/output`).
- `filename`: nome do arquivo (sem extensão).

Retorno
- `str`: mensagem de sucesso (no código: "arquivo xlsx salvo com sucesso").

Comportamento
- Garante que `output_path` existe (`os.makedirs(output_path, exist_ok=True)`).
- Gera `out_path = os.path.join(output_path, f"{filename}.xlsx")` e chama `df.to_excel(out_path, index=False)`.

Exemplo de uso

```python
from pipeline.load import load_to_excel
import pandas as pd

df = pd.DataFrame({"nome": ["ana", "bruno"], "valor": [10, 20]})
mensagem = load_to_excel(df, "data/output", "teste")
print(mensagem)  # "arquivo xlsx salvo com sucesso"
```

Observações
- `df.to_excel` usa o engine padrão (normalmente `openpyxl`) para arquivos `.xlsx`. Certifique-se de que `openpyxl` está instalado (está listado em `pyproject.toml`).
- Se o arquivo estiver aberto no Excel no Windows, a escrita pode falhar devido a bloqueio do arquivo.

---

## Como usar as funções individualmente (import e chamadas diretas)

Você pode importar e executar qualquer função do pipeline a partir do seu ambiente Python (por exemplo, dentro do REPL ou de um script):

```python
from pipeline.extract import extract_from_excel
from pipeline.transform import transform_data
from pipeline.load import load_to_excel

# executar as etapas manualmente
data_list = extract_from_excel("data/input")
if data_list:
    df = transform_data(data_list)
    load_to_excel(df, "data/output", "dados_concatenados")
else:
    print("Nenhum arquivo encontrado em data/input")
```

Recomenda-se rodar usando o Poetry (para garantir dependências corretas):

```powershell
poetry run python src/main.py
```

---

## Como testar e depurar funções

- Testes unitários já estão em `tests/` (use `pytest`).

Para rodar testes via Poetry:

```powershell
poetry run pytest -q
```

Dicas de depuração:
- Use `print(df.head())` nas etapas intermediárias para inspecionar os dados.
- Verifique o encoding e valores nulos após a leitura (`df.isna().sum()`).
- Para problemas de leitura, tente abrir o arquivo diretamente com `pandas.read_excel("caminho")` em um REPL.

---

## Boas práticas e melhorias sugeridas

- Adicionar tratamento de erros no `extract_from_excel` (capturar `pd.errors` e continuar com arquivos válidos).
- Validar esquema (colunas esperadas) antes de concatenar.
- Registrar logs em vez de usar `print()` (usar `logging` com níveis).
- Adicionar testes que criem arquivos Excel temporários (`tmp_path` do pytest) para validar o pipeline.

---

Página criada: `docs/pipeline.md`

Se quiser, eu posso:
- Incluir exemplos reais de arquivos Excel de amostra em `data/input/` (pequenos CSV convertidos para `.xlsx`).
- Gerar docstrings mais ricas para cada função diretamente nos arquivos `src/pipeline/*.py` e rodar os testes.
- Adicionar seções da API e exemplos copy-paste para notebooks.

---
