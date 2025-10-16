# pyenv (Windows PowerShell) — instalação e uso

Esta página mostra como instalar e usar o pyenv no Windows (via pyenv-win) e como integrá-lo com o Poetry. Inclui comandos passo a passo, exemplos de saída e lugares onde você pode colar screenshots/prints.

Atenção: não consigo gerar imagens aqui — adicione suas capturas em `docs/images/` e então remova o texto `![...](docs/images/...)` e substitua pelos caminhos corretos.

---

## 1. Por que usar pyenv?

- Permite ter múltiplas versões do Python instaladas lado a lado.
- Facilita garantir que o projeto use a versão exata especificada em `pyproject.toml`.
- Muito útil para desenvolver e testar código em diferentes versões do Python.

---

## 2. Instalação no Windows (pyenv-win) — PowerShell

Abra o PowerShell como usuário (não é necessário Administrador, mas necessário para alterar o perfil se quiser persistir variáveis de ambiente).

1) Clone o repositório pyenv-win:

```powershell
# Clona o pyenv-win para a pasta do usuário
git clone https://github.com/pyenv-win/pyenv-win.git $HOME\.pyenv
```

2) Adicione pyenv ao PATH no seu perfil do PowerShell (arquivo `$PROFILE`).

- Abra o perfil (se não existir, o comando criará um arquivo):

```powershell
notepad $PROFILE
```

- Cole as linhas abaixo no arquivo e salve:

```powershell
# pyenv-win
$env:PYENV = "$HOME\.pyenv\pyenv-win\bin"
$env:PATH = "$env:PYENV;$env:PATH"
```

- Reabra o PowerShell para aplicar as mudanças (ou rode `& $PROFILE` para recarregar).

3) Verifique a instalação:

```powershell
pyenv --version
```

Exemplo de saída esperada (sua versão pode variar):

```
pyenv 2.64.0
```

(Adicione aqui um screenshot do PowerShell mostrando o comando `pyenv --version`.)

Observação: coloque capturas em `docs/images/` e atualize o link acima para `images/pyenv-version.png` quando disponíveis.

---

## 3. Instalar uma versão do Python com pyenv (exemplo 3.12.7)

```powershell
pyenv install 3.12.7
```

Dependendo da conexão e do sistema, o download e build podem levar alguns minutos. Após instalar, verifique:

```powershell
pyenv versions
```

Saída esperada (exemplo):

```
* 3.12.7 (set by C:\Users\seuuser\.pyenv\pyenv-win\version)
  3.11.4
  3.10.12
```

(Adicione captura de `pyenv versions` se quiser)

---

## 4. Definir versão global e local

- Definir global (padrão para todo o sistema):

```powershell
pyenv global 3.12.7
```

- Definir local (apenas para o diretório do projeto — cria `.python-version`):

```powershell
cd G:\dev\Jornada_de_dados\estrutura_workshop
pyenv local 3.12.7
```

Verifique a versão ativa:

```powershell
python --version
# ou
pyenv which python
```

Exemplo de saída:

```
Python 3.12.7
```

---

## 5. Integrando pyenv com Poetry

Depois de definir a versão local do Python com `pyenv local`, peça ao Poetry para usar essa versão quando criar/associar o ambiente:

```powershell
cd G:\dev\Jornada_de_dados\estrutura_workshop
# Use o caminho do python fornecido por pyenv
poetry env use (pyenv which python)
```

Observação para PowerShell: o comando `poetry env use (pyenv which python)` pode precisar de substituição pelo caminho completo retornado por `pyenv which python`. Exemplo:

```powershell
$py = pyenv which python
poetry env use $py
```

Se o Poetry já tiver criado um ambiente para outra versão e você quiser trocar:

```powershell
poetry env list
poetry env remove <nome-do-ambiente>
poetry install
```

Após isso, rode os comandos usuais:

```powershell
poetry install
poetry run python src/main.py
```

(Adicione um screenshot do resultado de `poetry env use` e de `poetry run python src/main.py` se quiser)

---

## 6. Local das capturas / sugestões de imagens

- Coloque capturas em `docs/images/`.
- Referencie-as neste arquivo usando Markdown: `![descrição](images/nome.png)`.

Exemplo de imagens que ajudam:

- `images/pyenv-install.png` — saída do `git clone` e do PATH sendo adicionado.
- `images/pyenv-install-version.png` — `pyenv install 3.12.7` em execução.
- `images/pyenv-versions.png` — saída de `pyenv versions`.
- `images/poetry-env-use.png` — saída do `poetry env use` mostrando o ambiente criado.

---

## 7. Problemas comuns e soluções (Windows)

- Erro: `pyenv: command not found` — verifique se você adicionou `$HOME\.pyenv\pyenv-win\bin` ao PATH e reabriu o PowerShell.
- Erro: falha no `pyenv install` — pode faltar dependências do build; verifique logs e considere instalar o instalador do Windows Python em vez de compilar.
- Erro: Poetry não usa a versão correta — verifique `pyenv which python` e use o caminho absoluto com `poetry env use`.

---

## 8. Próximos passos

- Depois de ter o pyenv e Poetry configurados, rode `poetry install` e `poetry run mkdocs serve` para visualizar a documentação local.
- Se quiser, posso criar as imagens a partir do terminal (se você me enviar as saídas) ou posso adicionar instruções mais detalhadas para resolver erros de build do `pyenv install` no Windows.

---

Página criada: `docs/pyenv.md` — edite e adicione imagens em `docs/images/` conforme desejar.
