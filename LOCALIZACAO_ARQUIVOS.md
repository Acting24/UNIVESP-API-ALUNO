# 📍 Localização dos Arquivos do Projeto

Este documento descreve a localização e organização de todos os arquivos criados para o projeto API REST para Alunos da Univesp.

## 🗂️ Diretório Principal

Todos os arquivos estão localizados no diretório:

```
C:\Users\dell\univesp_api_alunos\
```

## 📋 Estrutura Completa dos Arquivos Criados

### 📁 Raiz do Projeto
**Localização:** `C:\Users\dell\univesp_api_alunos\`

| Arquivo | Descrição | Tipo |
|---------|-----------|------|
| `manage.py` | Script de gerenciamento Django | Python |
| `requirements.txt` | Lista de dependências do projeto | Texto |
| `django.bat` | Script batch para comandos Django | Batch |
| `start_server.py` | Script para iniciar o servidor | Python |
| `demo_api.py` | Script de demonstração da API | Python |
| `listar_alunos.py` | Script para listar alunos cadastrados | Python |
| `exemplo_frontend.html` | Interface web de exemplo com W3.CSS | HTML |
| `README.md` | Documentação principal do projeto | Markdown |
| `PROJETO_COMPLETO.md` | Documentação técnica completa | Markdown |
| `LOCALIZACAO_ARQUIVOS.md` | Este documento (localização dos arquivos) | Markdown |
| `db.sqlite3` | Banco de dados SQLite | Database |

### 📁 Aplicação Alunos
**Localização:** `C:\Users\dell\univesp_api_alunos\alunos\`

| Arquivo | Descrição | Função |
|---------|-----------|--------|
| `models.py` | Modelo de dados do Aluno | Define estrutura do banco |
| `serializers.py` | Serializers para API REST | Conversão JSON ↔ Modelo |
| `views.py` | ViewSets da API com operações CRUD | Lógica da API |
| `admin.py` | Configuração do admin Django | Interface administrativa |
| `urls.py` | URLs da aplicação | Roteamento |
| `apps.py` | Configuração da aplicação | Configuração Django |
| `tests.py` | Arquivo de testes (padrão Django) | Testes unitários |
| `__init__.py` | Inicializador do módulo Python | Módulo Python |

### 📁 Migrações do Banco de Dados
**Localização:** `C:\Users\dell\univesp_api_alunos\alunos\migrations\`

| Arquivo | Descrição |
|---------|-----------|
| `0001_initial.py` | Migração inicial do banco de dados |
| `__init__.py` | Inicializador do módulo |

### 📁 Configurações do Projeto Django
**Localização:** `C:\Users\dell\univesp_api_alunos\univesp_project\`

| Arquivo | Descrição | Função |
|---------|-----------|--------|
| `settings.py` | Configurações principais do Django | Configuração geral |
| `urls.py` | URLs principais do projeto | Roteamento principal |
| `wsgi.py` | Interface WSGI para produção | Deploy web |
| `asgi.py` | Interface ASGI para aplicações assíncronas | Deploy assíncrono |
| `__init__.py` | Inicializador do módulo | Módulo Python |

### 📁 Ambiente Virtual
**Localização:** `C:\Users\dell\univesp_api_alunos\venv\`

**Conteúdo:**
- ✅ Todas as dependências Python instaladas
- ✅ Django 5.2.5
- ✅ Django REST Framework 3.16.1
- ✅ django-cors-headers
- ✅ django-filter
- ✅ requests
- ✅ Scripts de ativação do ambiente virtual

## 🎯 Resumo da Organização

### 📊 Estatísticas dos Arquivos

| Categoria | Quantidade | Localização |
|-----------|------------|-------------|
| **Arquivos principais** | 11 | Raiz do projeto |
| **Código da aplicação** | 8 | `/alunos/` |
| **Migrações** | 2 | `/alunos/migrations/` |
| **Configurações Django** | 5 | `/univesp_project/` |
| **Dependências** | ~50+ | `/venv/` |

### 🔧 Scripts Principais de Uso

| Script | Comando | Função |
|--------|---------|--------|
| **Iniciar servidor** | `.\django.bat runserver` | Executar API |
| **Testar API** | `python demo_api.py` | Demonstração completa |
| **Listar alunos** | `python listar_alunos.py` | Ver dados cadastrados |
| **Frontend web** | Abrir `exemplo_frontend.html` | Interface web |
| **Migrações** | `.\django.bat migrate` | Atualizar banco |

### 📚 Documentação Disponível

| Arquivo | Tipo | Conteúdo |
|---------|------|----------|
| `README.md` | Guia de uso | Instruções rápidas de instalação e uso |
| `PROJETO_COMPLETO.md` | Documentação técnica | Código completo e estrutura detalhada |
| `LOCALIZACAO_ARQUIVOS.md` | Mapa de arquivos | Este documento com localização de tudo |

## 🚀 Como Navegar no Projeto

### 1. **Começar pelo README.md**
```bash
C:\Users\dell\univesp_api_alunos\README.md
```

### 2. **Ver código principal em:**
```bash
C:\Users\dell\univesp_api_alunos\alunos\models.py      # Modelo de dados
C:\Users\dell\univesp_api_alunos\alunos\views.py       # API endpoints
C:\Users\dell\univesp_api_alunos\alunos\serializers.py # Conversores JSON
```

### 3. **Configurações importantes:**
```bash
C:\Users\dell\univesp_api_alunos\univesp_project\settings.py  # Django config
C:\Users\dell\univesp_api_alunos\univesp_project\urls.py      # URLs principais
```

### 4. **Scripts de teste:**
```bash
C:\Users\dell\univesp_api_alunos\demo_api.py          # Demonstração
C:\Users\dell\univesp_api_alunos\listar_alunos.py     # Listar dados
```

### 5. **Frontend de exemplo:**
```bash
C:\Users\dell\univesp_api_alunos\exemplo_frontend.html # Interface web
```

## 📂 Comandos de Navegação

### PowerShell/CMD
```powershell
# Ir para o diretório do projeto
cd C:\Users\dell\univesp_api_alunos

# Listar arquivos principais
dir

# Ver estrutura completa
tree /F

# Abrir no explorador
explorer .
```

### Abrir arquivos específicos
```bash
# Documentação principal
notepad README.md

# Código do modelo
notepad alunos\models.py

# Configurações
notepad univesp_project\settings.py

# Frontend
start exemplo_frontend.html
```

## 🎯 Pontos de Acesso Principais

### 🌐 URLs de Acesso
- **API REST**: http://127.0.0.1:8000/api/
- **Admin Django**: http://127.0.0.1:8000/admin/
- **Frontend**: `exemplo_frontend.html` (arquivo local)

### 💾 Backup dos Arquivos
Para criar backup do projeto:
```powershell
# Copiar pasta completa (excluindo venv)
robocopy "C:\Users\dell\univesp_api_alunos" "C:\Backup\univesp_api_backup" /E /XD venv
```

### 🔄 Restaurar Projeto
Para restaurar em outro local:
```bash
1. Copiar arquivos (exceto venv/)
2. Criar novo ambiente virtual: python -m venv venv
3. Instalar dependências: pip install -r requirements.txt
4. Executar migrações: python manage.py migrate
```

---

## 📝 Notas Importantes

### ✅ Arquivos Essenciais (NÃO deletar)
- `manage.py` - Essencial para Django
- `db.sqlite3` - Banco de dados com dados
- `requirements.txt` - Lista de dependências
- Pasta `alunos/` - Código principal da aplicação
- Pasta `univesp_project/` - Configurações Django

### ⚠️ Arquivos Opcionais
- `demo_api.py` - Pode ser removido após testes
- `listar_alunos.py` - Script auxiliar
- `exemplo_frontend.html` - Exemplo, pode ser customizado

### 🔧 Arquivos Auto-gerados
- `db.sqlite3` - Criado automaticamente
- Pasta `__pycache__/` - Cache do Python
- Arquivos `.pyc` - Bytecode compilado

---

**📍 Localização Base:** `C:\Users\dell\univesp_api_alunos\`

**📅 Data de Criação:** 31/08/2025

**🔧 Versão do Projeto:** 1.0

**👨‍💻 Tecnologias:** Django 5.2.5 + Django REST Framework 3.16.1 + W3.CSS
