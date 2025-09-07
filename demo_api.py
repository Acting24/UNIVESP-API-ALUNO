#!/usr/bin/env python
"""
Script de demonstração da API REST para Alunos da Univesp
"""

import requests
import json
from datetime import datetime, date

# Configurações da API
API_BASE_URL = "http://127.0.0.1:8000/api"
HEADERS = {"Content-Type": "application/json"}


def criar_alunos_exemplo():
    """Cria alguns alunos de exemplo na API"""
    
    alunos_exemplo = [
        {
            "ra": "2024001001",
            "nome_completo": "João Silva Santos",
            "email": "joao.silva@aluno.univesp.br",
            "curso": "ENG_COMP",
            "semestre_atual": 3,
            "data_ingresso": "2023-02-01",
            "ativo": True,
            "polo": "São Paulo - Bela Vista",
            "telefone": "(11) 99999-1111"
        },
        {
            "ra": "2024001002",
            "nome_completo": "Maria Oliveira Costa",
            "email": "maria.oliveira@aluno.univesp.br", 
            "curso": "CIENCIA_DADOS",
            "semestre_atual": 2,
            "data_ingresso": "2023-08-01",
            "ativo": True,
            "polo": "São Paulo - Liberdade",
            "telefone": "(11) 99999-2222"
        },
        {
            "ra": "2024001003",
            "nome_completo": "Pedro Henrique Lima",
            "email": "pedro.lima@aluno.univesp.br",
            "curso": "TEC_INFO",
            "semestre_atual": 4,
            "data_ingresso": "2022-08-01",
            "ativo": True,
            "polo": "Campinas",
            "telefone": "(19) 99999-3333"
        },
        {
            "ra": "2024001004",
            "nome_completo": "Ana Carolina Ferreira",
            "email": "ana.ferreira@aluno.univesp.br",
            "curso": "MATEMATICA",
            "semestre_atual": 1,
            "data_ingresso": "2024-02-01",
            "ativo": True,
            "polo": "Santos",
            "telefone": "(13) 99999-4444"
        }
    ]
    
    print("=== CRIANDO ALUNOS DE EXEMPLO ===")
    for aluno in alunos_exemplo:
        try:
            response = requests.post(f"{API_BASE_URL}/alunos/", 
                                   data=json.dumps(aluno), 
                                   headers=HEADERS)
            if response.status_code == 201:
                print(f"✓ Aluno {aluno['nome_completo']} criado com sucesso")
            else:
                print(f"✗ Erro ao criar {aluno['nome_completo']}: {response.text}")
        except requests.exceptions.ConnectionError:
            print("✗ Erro: Não foi possível conectar à API. Certifique-se de que o servidor está rodando.")
            return False
    
    return True


def testar_endpoints():
    """Testa todos os endpoints da API"""
    
    print("\n=== TESTANDO ENDPOINTS DA API ===")
    
    # 1. Listar todos os alunos
    try:
        response = requests.get(f"{API_BASE_URL}/alunos/")
        if response.status_code == 200:
            data = response.json()
            print(f"✓ GET /api/alunos/ - {data['count']} alunos encontrados")
        else:
            print(f"✗ Erro ao listar alunos: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("✗ Erro: Servidor não está respondendo")
        return
    
    # 2. Listar apenas alunos ativos
    response = requests.get(f"{API_BASE_URL}/alunos/ativos/")
    if response.status_code == 200:
        data = response.json()
        print(f"✓ GET /api/alunos/ativos/ - {data['total_alunos_ativos']} alunos ativos")
    
    # 3. Estatísticas
    response = requests.get(f"{API_BASE_URL}/alunos/estatisticas/")
    if response.status_code == 200:
        data = response.json()
        print(f"✓ GET /api/alunos/estatisticas/ - Total: {data['total_alunos']}")
        print(f"  Distribuição por curso: {data['distribuicao_por_curso']}")
    
    # 4. Filtrar por curso
    response = requests.get(f"{API_BASE_URL}/alunos/por_curso/?curso=ENG_COMP")
    if response.status_code == 200:
        data = response.json()
        print(f"✓ GET /api/alunos/por_curso/?curso=ENG_COMP - {data['total_alunos']} alunos de Engenharia da Computação")
    
    # 5. Buscar alunos
    response = requests.get(f"{API_BASE_URL}/alunos/?search=João")
    if response.status_code == 200:
        data = response.json()
        print(f"✓ GET /api/alunos/?search=João - {data['count']} resultados encontrados")
    
    # 6. Filtrar por semestre
    response = requests.get(f"{API_BASE_URL}/alunos/?semestre_atual=3")
    if response.status_code == 200:
        data = response.json()
        print(f"✓ GET /api/alunos/?semestre_atual=3 - {data['count']} alunos no 3º semestre")


def main():
    """Função principal do script de demonstração"""
    
    print("🎓 DEMO - API REST para Alunos da Univesp")
    print("=" * 50)
    
    # Primeiro, criar dados de exemplo
    if criar_alunos_exemplo():
        # Depois, testar os endpoints
        testar_endpoints()
    
    print("\n=== RESUMO DOS ENDPOINTS DISPONÍVEIS ===")
    endpoints = [
        "GET    /api/alunos/                     - Listar todos os alunos",
        "POST   /api/alunos/                     - Criar novo aluno",
        "GET    /api/alunos/{id}/                - Obter aluno específico",
        "PUT    /api/alunos/{id}/                - Atualizar aluno",
        "DELETE /api/alunos/{id}/                - Excluir aluno",
        "GET    /api/alunos/ativos/              - Listar alunos ativos",
        "GET    /api/alunos/estatisticas/        - Estatísticas gerais",
        "GET    /api/alunos/por_curso/?curso=X   - Alunos por curso",
        "POST   /api/alunos/{id}/ativar/         - Ativar aluno",
        "POST   /api/alunos/{id}/desativar/      - Desativar aluno",
        "",
        "Parâmetros de filtro e busca:",
        "?curso=CURSO_CODE                      - Filtrar por curso",
        "?ativo=true/false                      - Filtrar por status",
        "?semestre_atual=N                      - Filtrar por semestre",
        "?search=TERMO                          - Buscar em nome, RA ou email",
        "?ordering=campo                        - Ordenar por campo"
    ]
    
    for endpoint in endpoints:
        print(endpoint)
    
    print("\n🌐 Acesso:")
    print("- API REST: http://127.0.0.1:8000/api/")
    print("- Admin Django: http://127.0.0.1:8000/admin/")
    print("- Login admin: admin / admin123")


if __name__ == "__main__":
    main()
