# API REST para Alunos da Univesp

Este projeto implementa um serviço web REST no Django para manipular dados de alunos da Universidade Virtual do Estado de São Paulo (Univesp).

## 🎯 Características

- **API REST completa** para operações CRUD com dados de alunos
- **Modelo de dados** específico para alunos da Univesp com validações
- **Endpoints personalizados** para consultas específicas (por curso, estatísticas, etc.)
- **Interface administrativa** Django para gerenciamento manual
- **Filtros e busca** avançados
- **Paginação** automática
- **CORS** configurado para desenvolvimento web

## 🏗️ Estrutura do Projeto

```
univesp_api_alunos/
├── manage.py                 # Script de gerenciamento do Django
├── requirements.txt          # Dependências do projeto
├── demo_api.py              # Script de demonstração da API
├── db.sqlite3               # Banco de dados SQLite
├── univesp_project/         # Configurações do projeto Django
│   ├── settings.py          # Configurações principais
│   ├── urls.py              # URLs principais
│   └── ...
├── alunos/                  # Aplicação Django para alunos
│   ├── models.py            # Modelo de dados do Aluno
│   ├── serializers.py       # Serializers para API REST
│   ├── views.py             # ViewSets da API
│   ├── admin.py             # Configuração do admin
│   └── ...
└── venv/                    # Ambiente virtual Python
```

## 📊 Modelo de Dados - Aluno

### Campos principais:
- **RA**: Registro Acadêmico (10 dígitos, único)
- **Nome Completo**: Nome completo do aluno
- **Email**: Email institucional (único)
- **Curso**: Curso do aluno (escolha entre cursos da Univesp)
- **Semestre Atual**: Semestre que está cursando (1-10)
- **Data de Ingresso**: Data de entrada no curso
- **Ativo**: Status do aluno no curso
- **Polo**: Polo de apoio presencial (opcional)
- **Telefone**: Contato telefônico (opcional)

### Cursos disponíveis:
- Engenharia da Computação
- Ciência de Dados
- Tecnologia da Informação
- Matemática
- Física
- Química
- Biologia
- Pedagogia
- Letras
- Administração

## 🚀 Como usar

### 1. Instalar dependências:
```bash
# Ativar ambiente virtual (se não estiver ativado)
venv\Scripts\activate.bat  # Windows
# ou use diretamente:
venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 2. Executar migrações:
```bash
# Opção 1: Usar o ambiente virtual diretamente
venv\Scripts\python.exe manage.py migrate

# Opção 2: Usar o script batch (mais fácil)
.\django.bat migrate
```

### 3. Iniciar servidor:
```bash
# Opção 1: Usar o ambiente virtual diretamente
venv\Scripts\python.exe manage.py runserver

# Opção 2: Usar o script batch
.\django.bat runserver

# Opção 3: Usar o script Python dedicado
python start_server.py
```

### 4. Acessar a API:
- **API REST**: http://127.0.0.1:8000/api/
- **Admin Django**: http://127.0.0.1:8000/admin/ (admin/admin123)

## 🔗 Endpoints da API

### Operações CRUD básicas:
- `GET /api/alunos/` - Listar todos os alunos
- `POST /api/alunos/` - Criar novo aluno
- `GET /api/alunos/{id}/` - Obter aluno específico
- `PUT /api/alunos/{id}/` - Atualizar aluno
- `PATCH /api/alunos/{id}/` - Atualização parcial
- `DELETE /api/alunos/{id}/` - Excluir aluno

### Endpoints especiais:
- `GET /api/alunos/ativos/` - Listar apenas alunos ativos
- `GET /api/alunos/estatisticas/` - Estatísticas gerais
- `GET /api/alunos/por_curso/?curso=CODIGO` - Alunos por curso específico
- `POST /api/alunos/{id}/ativar/` - Ativar um aluno
- `POST /api/alunos/{id}/desativar/` - Desativar um aluno

### Parâmetros de filtro e busca:
- `?curso=CODIGO` - Filtrar por código do curso
- `?ativo=true/false` - Filtrar por status ativo/inativo
- `?semestre_atual=N` - Filtrar por semestre
- `?search=TERMO` - Buscar em nome, RA ou email
- `?ordering=campo` - Ordenar por campo específico

## 📝 Exemplos de uso

### Criar um novo aluno:
```bash
curl -X POST http://127.0.0.1:8000/api/alunos/ \
  -H "Content-Type: application/json" \
  -d '{
    "ra": "2024001005",
    "nome_completo": "Carlos Eduardo Silva",
    "email": "carlos.silva@aluno.univesp.br",
    "curso": "ENG_COMP",
    "semestre_atual": 1,
    "data_ingresso": "2024-02-01",
    "ativo": true,
    "polo": "São Paulo - Centro"
  }'
```

### Buscar alunos:
```bash
# Buscar por nome
curl "http://127.0.0.1:8000/api/alunos/?search=João"

# Filtrar por curso
curl "http://127.0.0.1:8000/api/alunos/?curso=CIENCIA_DADOS"

# Alunos do 3º semestre
curl "http://127.0.0.1:8000/api/alunos/?semestre_atual=3"
```

### Obter estatísticas:
```bash
curl "http://127.0.0.1:8000/api/alunos/estatisticas/"
```

## 🧪 Demonstração

Execute o script de demonstração para ver a API em funcionamento:

```bash
python demo_api.py
```

Este script irá:
1. Criar alunos de exemplo na API
2. Testar todos os endpoints disponíveis
3. Mostrar a documentação dos endpoints

## 🛠️ Tecnologias utilizadas

- **Django 5.2.5** - Framework web principal
- **Django REST Framework 3.16.1** - Para criação da API REST
- **django-cors-headers** - Para configuração de CORS
- **django-filter** - Para filtros avançados
- **SQLite** - Banco de dados (padrão para desenvolvimento)

## 📚 Próximos passos

Para expandir este projeto, você pode:

1. **Autenticação e autorização**: Implementar JWT ou sessões
2. **Documentação automática**: Usar django-rest-swagger ou drf-spectacular
3. **Testes automatizados**: Criar testes unitários e de integração
4. **Deploy**: Configurar para produção com PostgreSQL e Docker
5. **Frontend**: Criar interface web usando os frameworks mencionados nas videoaulas

---

*Projeto desenvolvido seguindo as diretrizes das videoaulas da Univesp sobre programação de aplicativos e framework W3.CSS*
