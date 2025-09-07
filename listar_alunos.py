#!/usr/bin/env python
import os
import django
import sys

# Configurar Django
sys.path.append('.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'univesp_project.settings')
django.setup()

from alunos.models import Aluno

def main():
    print("=" * 50)
    print("🎓 ALUNOS CADASTRADOS NA API UNIVESP")
    print("=" * 50)
    
    total = Aluno.objects.count()
    print(f"Total de alunos: {total}")
    
    if total > 0:
        print("\nLista de alunos:")
        for aluno in Aluno.objects.all():
            status = "✅ Ativo" if aluno.ativo else "❌ Inativo"
            print(f"- {aluno.nome_completo}")
            print(f"  RA: {aluno.ra}")
            print(f"  Email: {aluno.email}")
            print(f"  Curso: {aluno.get_curso_display_name()}")
            print(f"  Semestre: {aluno.semestre_atual}º")
            print(f"  Status: {status}")
            if aluno.polo:
                print(f"  Polo: {aluno.polo}")
            print()
    else:
        print("\nNenhum aluno cadastrado ainda.")
        print("Execute o script demo_api.py para criar dados de exemplo.")

if __name__ == "__main__":
    main()
