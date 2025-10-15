# Estrutura Workshop

Este repositório contém material do workshop "Jornada de Dados".

Como ativar o ambiente (PowerShell)

1. Descobrir o path do venv gerenciado pelo Poetry:

```powershell
poetry env info --path
```

2. Ativar o venv criado localmente (exemplo para este projeto):

```powershell
& 'G:\dev\Jornada_de_dados\estrutura_workshop\.venv\Scripts\Activate.ps1'
```

Executar comandos sem ativar o shell

```powershell
poetry run python -V
poetry run python script.py
```

Criar/instalar dependências

```powershell
poetry env use python
poetry install
```

Observação sobre 'touch' no PowerShell

- O comando `touch` é um utilitário típico de sistemas Unix (bash). No PowerShell use:

```powershell
# cria o arquivo README.md se não existir
New-Item README.md -ItemType File -Force
```

Ou no cmd.exe:

```bat
copy NUL README.md
```