# 🐍 Pyenv — Gerenciamento de Versões Python

Esta página mostra como instalar e usar o pyenv para gerenciar múltiplas versões do Python e integrá-lo com o Poetry.

---

## 🎯 Por que usar Pyenv?

### ✅ **Benefícios**:
- 🔄 **Múltiplas versões** do Python lado a lado
- 🎯 **Versão exata** especificada no `pyproject.toml`
- 🧪 **Teste** de código em diferentes versões
- 🔒 **Isolamento** entre projetos
- 🚀 **Troca rápida** entre versões

---

## 💻 Instalação por Sistema Operacional

### 🪟 Windows (pyenv-win)

#### 📥 **1. Instalar via Git**
```powershell
# Clone o repositório pyenv-win
git clone https://github.com/pyenv-win/pyenv-win.git $HOME\.pyenv
```

#### ⚙️ **2. Configurar PATH**
```powershell
# Abrir perfil do PowerShell
notepad $PROFILE

# Adicionar ao arquivo (copie e cole):
$env:PYENV = "$HOME\.pyenv\pyenv-win\bin"
$env:PATH = "$env:PYENV;$env:PATH"
```

#### 🔄 **3. Recarregar Terminal**
```powershell
# Recarregar perfil
& $PROFILE

# OU reiniciar PowerShell
```

#### ✅ **4. Verificar Instalação**
```powershell
pyenv --version
# Saída esperada: pyenv 2.64.0 (ou versão mais recente)
```

---

### 🍎 macOS

```bash
# Usando Homebrew (recomendado)
brew install pyenv

# Adicionar ao ~/.zshrc ou ~/.bash_profile
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

# Recarregar shell
source ~/.zshrc
```

---

### 🐧 Linux (Ubuntu/Debian)

```bash
# Instalar dependências
sudo apt-get update
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git

# Instalar pyenv
curl https://pyenv.run | bash

# Adicionar ao ~/.bashrc
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

# Recarregar shell
source ~/.bashrc
```

---

## 🚀 Usando o Pyenv

### 📋 **Comandos Essenciais**

#### 🔍 **Listar versões disponíveis**
```bash
pyenv install --list
# Mostra todas as versões disponíveis para instalação
```

#### 📥 **Instalar versão específica**
```bash
# Instalar Python 3.12.7 (versão do projeto)
pyenv install 3.12.7
```

#### 📊 **Listar versões instaladas**
```bash
pyenv versions
# Exemplo de saída:
#   system
# * 3.12.7 (set by /path/to/.python-version)
#   3.11.4
#   3.10.12
```

#### 🌍 **Definir versão global (sistema)**
```bash
pyenv global 3.12.7
```

#### 📁 **Definir versão local (projeto)**
```bash
cd estrutura_workshop
pyenv local 3.12.7
# Cria arquivo .python-version
```

#### ✅ **Verificar versão ativa**
```bash
python --version
# ou
pyenv which python
```

---

## 🔗 Integração com Poetry

### ⚙️ **Configuração Recomendada**

#### 1️⃣ **Definir versão local do projeto**
```bash
cd estrutura_workshop
pyenv local 3.12.7
```

#### 2️⃣ **Configurar Poetry para usar pyenv**
```bash
# Opção 1: Usar versão atual
poetry env use python

# Opção 2: Usar caminho específico
poetry env use $(pyenv which python)

# Windows PowerShell:
$py = pyenv which python
poetry env use $py
```

#### 3️⃣ **Verificar configuração**
```bash
poetry env info
# Deve mostrar Python 3.12.7
```

#### 4️⃣ **Instalar dependências**
```bash
poetry install
```

---

## 🔄 Workflow Típico

### 📝 **Para Novo Projeto**
```bash
# 1. Navegar para diretório do projeto
cd meu-projeto

# 2. Definir versão Python
pyenv local 3.12.7

# 3. Configurar Poetry
poetry env use python
poetry install

# 4. Ativar ambiente
poetry shell
```

### 🔧 **Para Projeto Existente**
```bash
# 1. Clonar repositório
git clone <repo-url>
cd projeto

# 2. Pyenv detecta versão automaticamente (.python-version)
python --version

# 3. Se necessário, instalar versão
pyenv install 3.12.7

# 4. Configurar Poetry
poetry env use python
poetry install
```

---

## 🛠️ Solução de Problemas

### ❌ **"pyenv: command not found"**

#### 🪟 **Windows**:
```powershell
# Verificar se PATH foi adicionado
echo $env:PATH | Select-String "pyenv"

# Recarregar perfil
& $PROFILE

# Verificar se diretório existe
Test-Path "$HOME\.pyenv\pyenv-win\bin"
```

#### 🍎 **macOS/Linux**:
```bash
# Verificar instalação
which pyenv

# Recarregar shell config
source ~/.zshrc  # ou ~/.bashrc
```

---

### ❌ **Falha no "pyenv install"**

#### 🪟 **Windows**:
- **Problema**: Falha no download/compilação
- **Solução**: Usar instalador oficial do Python

#### 🐧 **Linux**:
```bash
# Instalar dependências em falta
sudo apt-get install -y build-essential libssl-dev zlib1g-dev
```

---

### ❌ **Poetry não usa versão correta**

```bash
# Verificar versão atual
pyenv which python
python --version

# Forçar Poetry a usar versão específica
poetry env remove python  # Remove ambiente existente
poetry env use $(pyenv which python)
poetry install
```

---

### ❌ **Arquivo .python-version ignorado**

```bash
# Verificar se arquivo existe
cat .python-version

# Verificar se pyenv está detectando
pyenv version

# Se necessário, recriar
pyenv local 3.12.7
```

---

## 📊 Comandos de Referência

### 🔍 **Informações**
```bash
pyenv --version          # Versão do pyenv
pyenv versions           # Versões instaladas
pyenv which python       # Caminho do Python ativo
pyenv root              # Diretório de instalação
```

### 🎯 **Versões**
```bash
pyenv install --list    # Versões disponíveis
pyenv install 3.12.7    # Instalar versão
pyenv uninstall 3.11.0  # Desinstalar versão
```

### ⚙️ **Configuração**
```bash
pyenv global 3.12.7     # Versão global
pyenv local 3.12.7      # Versão local (projeto)
pyenv shell 3.11.0      # Versão temporária (sessão)
```

---

## 🔗 Próximos Passos

Agora que o Pyenv está configurado:

- ⚙️ **Configure o Projeto**: [⚙️ Setup](setup.md)
- 🚀 **Execute o Pipeline**: [📋 Pipeline](pipeline.md)
- 🧪 **Execute os Testes**: [🧪 Tests](tests.md)
- 🔍 **Configure Pre-commit**: [🔍 Pre-commit](precommit.md)
