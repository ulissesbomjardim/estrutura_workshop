# ⚙️ Setup — Configuração do Ambiente

Esta página mostra passo a passo como configurar sua máquina para rodar este projeto: instalar o Python, Poetry e executar a configuração inicial.

---

## 🎯 Visão Geral

Para executar este projeto você precisará de:

- 🐍 **Python 3.12.7** (versão específica do projeto)
- 📦 **Poetry** (gerenciador de dependências)
- 💻 **Terminal/PowerShell** configurado

---

## 🐍 1. Instalar Python

### 📥 Download e Instalação

1. **Baixe o Python**: Acesse [python.org/downloads](https://www.python.org/downloads/)
2. **Versão recomendada**: `Python 3.12.7` (conforme `pyproject.toml`)

### ⚠️ Importante no Windows:
- ✅ **Marque "Add Python to PATH"** durante a instalação
- ✅ **Marque "Install for all users"** (recomendado)

### ✅ Verificar Instalação:
```bash
python --version
# Deve mostrar: Python 3.12.7
```

---

## 📦 2. Instalar Poetry

### 🪟 Windows (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

### 🍎 macOS / 🐧 Linux

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### ✅ Verificar Instalação:
```bash
poetry --version
# Deve mostrar: Poetry (version 1.x.x)
```

---

## 🔧 3. Configurar PATH (se necessário)

Se o comando `poetry` não for reconhecido:

### 🪟 Windows:
- Adicione ao PATH: `%USERPROFILE%\AppData\Roaming\Python\Scripts`

### 🍎 macOS / 🐧 Linux:
- Adicione ao PATH: `~/.local/bin`

### 🔄 Reinicie o terminal após alterar o PATH

---

## 🚀 4. Configurar o Projeto

### 📁 Clone o Repositório:
```bash
git clone <URL-DO-REPO>
cd estrutura_workshop
```

### 📦 Instalar Dependências:
```bash
poetry install
```

Este comando irá:
- ✅ Criar ambiente virtual automaticamente
- ✅ Instalar todas as dependências do `pyproject.toml`
- ✅ Instalar dependências de desenvolvimento (pytest, black, etc.)

### 🔍 Verificar Ambiente:
```bash
poetry env info
```

---

## ⚡ 5. Primeiros Comandos

### 🧪 Executar Testes:
```bash
poetry run pytest -q
```

### 🚀 Executar Pipeline:
```bash
poetry run python src/main.py
```

### 🐚 Ativar Shell do Poetry:
```bash
poetry shell
# Agora você pode usar comandos diretos:
python src/main.py
pytest -q
```

### 📖 Visualizar Documentação:
```bash
poetry run mkdocs serve
```

---

## 🛠️ Alternativas e Opções Avançadas

### 🐍 Usando Pyenv (Recomendado para Múltiplas Versões)

Se você trabalha com diferentes projetos Python:

1. **Instale o Pyenv**: Veja [📋 Pyenv](pyenv.md)
2. **Configure a versão**:
   ```bash
   pyenv install 3.12.7
   pyenv local 3.12.7
   ```
3. **Configure Poetry**:
   ```bash
   poetry env use 3.12.7
   ```

### 🔧 Problemas Comuns

#### ❌ `poetry install` falha (Linux):
**Solução**: Instale dependências do sistema:
```bash
sudo apt-get install build-essential libssl-dev zlib1g-dev
```

#### ❌ `poetry` não reconhecido:
**Solução**: Verifique se está no PATH ou reinstale
```bash
# Reinstalar Poetry
curl -sSL https://install.python-poetry.org | python3 - --uninstall
curl -sSL https://install.python-poetry.org | python3 -
```

#### ❌ Versão errada do Python:
**Solução**: Force a versão correta:
```bash
poetry env use python3.12
# ou caminho completo:
poetry env use /usr/bin/python3.12
```

---

## ✅ Checklist de Verificação

Antes de continuar, certifique-se de que:

- [ ] 🐍 Python 3.12.7 está instalado
- [ ] 📦 Poetry está funcionando (`poetry --version`)
- [ ] 📁 Projeto foi clonado localmente
- [ ] 🔧 `poetry install` executado com sucesso
- [ ] 🧪 Testes passam (`poetry run pytest -q`)

---

## 🔗 Próximos Passos

Agora que o ambiente está configurado:

- 🚀 **Execute o Pipeline**: [📋 Pipeline](pipeline.md)
- 🧪 **Execute os Testes**: [🧪 Tests](tests.md)
- 🔄 **Configure CI/CD**: [🚀 CI](ci.md)
- 📖 **Explore o Código**: [💻 Documentação do Código](codigo.md)
