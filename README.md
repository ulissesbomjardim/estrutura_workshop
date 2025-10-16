# Data Project Starter Kit

[![Codecov](https://img.shields.io/badge/coverage-unknown-lightgrey)](https://codecov.io/gh/ulissesbomjardim/estrutura_workshop)

## Documentação

A documentação do projeto está publicada em:

- https://ulissesbomjardim.github.io/estrutura_workshop/

## Sobre o Projeto

Este repositório é uma parte integrante do workshop "Como estruturar um projeto de dados do Zero". O intuito aqui é fornecer uma base e uma estrutura padronizada para iniciar projetos de engenharia, ciência e análise de dados. O foco principal é em boas práticas, automação, testes e documentação.

**Novo workshop disponível em 29/01!**

### Objetivos do Workshop:

* **Entender a estrutura padrão de projetos**: Isso inclui a organização de diretórios, como o código-fonte, testes, documentação, entre outros.
* **Estruturas padrões em projetos de dados**: Vamos refatorar o projeto utilizando classes, módulos e boas práticas em uma ETL.
* **Familiarizar-se com ferramentas de desenvolvimento**: Abordaremos o uso de ambientes virtuais e discutiremos ferramentas como PIP, CONDA e POETRY.
* **Testes com Pytest**: Garanta que seu código funcione como esperado, criando testes unitários e de integração.
* **Versionamento com Git e GitHub**: Aprenda a versionar seu projeto e a usar o GitHub para colaboração e publicação.
* **Documentação com MKDocs**: Você vai aprender a documentar seu projeto com MKDocs e a publicar sua documentação no GitHub Pages.
* **Automatização e CI/CD**: Configurar rotinas de integração e entrega contínua para manter a qualidade do projeto.

## Começando

### Pré-requisitos

* **VSCode**: É o editor de código que vamos utilizar no workshop. [Instruções de instalação do VSCode aqui](https://code.visualstudio.com/download).
* **Git e GitHub**:

  1. Você deve ter o Git instalado em sua máquina. [Instruções de instalação do Git aqui](https://git-scm.com/book/pt-br/v2).
  2. Você também deve ter uma conta no GitHub. [Instruções de criação de conta no GitHub aqui](https://docs.github.com/pt/get-started/onboarding/getting-started-with-your-github-account).
  3. Se você for usuário Windows, recomendo esse vídeo: [Youtube](https://www.youtube.com/watch?v=_hZf1teRFNg).
  4. Tutorial de Git e Github básico [Ebook](https://www.linkedin.com/feed/update/urn:li:activity:7093915148351864832/).
* **Python 3.12.7**: Este projeto utiliza Python 3.12.7. Recomendamos usar o Pyenv para gerenciar versões do Python.

  - **Pyenv**: [Instruções de instalação do Pyenv aqui](https://github.com/pyenv/pyenv#installation).
  - Para usuários Windows: [Tutorial Pyenv Windows](https://www.youtube.com/watch?v=TkcqjLu1dgA).
* **Poetry**: Este projeto utiliza Poetry para gerenciamento de dependências. [Instruções de instalação do Poetry aqui](https://python-poetry.org/docs/#installation).

  - Para usuários Windows: [Tutorial Poetry](https://www.youtube.com/watch?v=BuepZYn1xT8).
  - Instalação simples: `pip install poetry`

### Configuração do Projeto após Clonar

1. **Clone o repositório**:

```bash
git clone https://github.com/ulissesbomjardim/estrutura_workshop.git
cd estrutura_workshop
```

2. **Configure a versão correta do Python com Pyenv** (se usando Pyenv):

```bash
pyenv install 3.12.7
pyenv local 3.12.7
```

**Nota**: O projeto já possui um arquivo `.python-version` que especifica a versão Python 3.12.7.

3. **Configure o Poetry para usar a versão correta do Python**:

```bash
poetry env use 3.12.7
```

4. **Instale as dependências do projeto**:

```bash
poetry install
```

Este comando irá:

- Criar um ambiente virtual automaticamente
- Instalar todas as dependências do arquivo `pyproject.toml`
- Instalar dependências de desenvolvimento (pytest, black, isort, etc.)

5. **Ative o ambiente virtual** (opcional, mas recomendado):

```bash
poetry shell
```

### Executando o Projeto

6. **Execute os testes para garantir que tudo está funcionando**:

```bash
task test
```

ou se não estiver no shell do Poetry:

```bash
poetry run task test
```

7. **Execute a pipeline ETL**:

```bash
task run
```

ou:

```bash
poetry run task run
```

Este comando executará o arquivo `src/main.py` que processa arquivos Excel da pasta `data/input/` e gera o resultado em `data/output/`.

8. **Execute a documentação** (opcional):

```bash
task doc
```

ou:

```bash
poetry run task doc
```

Isso iniciará um servidor local com a documentação do MkDocs.

9. **Verifique se o arquivo foi gerado corretamente** na pasta `data/output/`.

### Comandos Úteis

#### Formatação de Código:

```bash
# recomendado: invoke via poetry (não precisa ativar o venv manualmente)
poetry run task format

# alternativa: ative o venv do poetry e rode sem 'poetry run'
$path = poetry env info --path
& "$path\Scripts\Activate.ps1"
task format
```

#### Ativação Manual do Ambiente Virtual:

Se preferir ativar o ambiente virtual manualmente:

```bash
# Descobrir o caminho do ambiente virtual
poetry env info --path

# Ativar o ambiente (Windows PowerShell)
$path = poetry env info --path
& "$path\Scripts\Activate.ps1"

# Ativar o ambiente (Windows CMD)
poetry env info --path
# Copie o caminho e execute: <caminho>\Scripts\activate.bat

# Ativar o ambiente (Linux/Mac)
source $(poetry env info --path)/bin/activate
```

#### Executar Testes com Coverage:

```bash
poetry run pytest --cov=src --cov-report=xml
```

#### Verificar informações do ambiente Poetry:

```bash
poetry env info
```

### Estrutura do Projeto

```
estrutura_workshop/
├── src/                    # Código fonte
│   ├── main.py            # Script principal da ETL
│   └── pipeline/          # Módulos do pipeline
│       ├── extract.py     # Extração de dados
│       ├── transform.py   # Transformação de dados
│       └── load.py        # Carregamento de dados
├── tests/                 # Testes unitários
├── data/
│   ├── input/            # Dados de entrada (arquivos Excel)
│   └── output/           # Dados processados (saída)
├── docs/                 # Documentação
├── pyproject.toml        # Configuração do projeto e dependências
├── poetry.lock           # Lock file das dependências
└── README.md             # Este arquivo
```

### Leituras Recomendadas

- [Ebook 1 - Testes](https://www.linkedin.com/feed/update/urn:li:activity:7099722252144848896/)
- [Ebook 2 - Github Actions](https://www.linkedin.com/feed/update/urn:li:activity:7098264928553201665/)
- [Ebook 3 - Na minha máquina funciona](https://www.linkedin.com/feed/update/urn:li:activity:7095419109449814017/)

### Referências

- **Repositório Original do Starter Kit**: [DataProjectStarterKit](https://github.com/lvgalvao/DataProjectStarterKit)
- **Repositório Base do Workshop**: [estrutura_workshop](https://github.com/lvgalvao/estrutura_workshop)
- **Site da Jornada de Dados**: [suajornadadedados.com.br](https://suajornadadedados.com.br/)

### Solução de Problemas

#### Problema com versão do Python:

Se você receber erros relacionados à versão do Python, certifique-se de que:

1. O Python 3.12.7 está instalado em seu sistema
2. O Poetry está configurado para usar a versão correta: `poetry env use 3.12.7`

#### Problemas com dependências:

Se houver conflitos de dependências:

1. Remova o ambiente virtual: `poetry env remove 3.12.7`
2. Recrie o ambiente: `poetry install`

#### Verificar se o Poetry está funcionando:

```bash
poetry --version
poetry env list
```

## Contato

Para dúvidas, sugestões ou feedbacks:

* **Ulisses bomjardim** - [ulisses.bomjardim@gmail.com](mailto:lvgalvaofilho@gmail.com)

---

*Updated: 2025-10-16*
