import subprocess
import sys
import time
import os

def start_server():
    """Inicia o servidor Django"""
    print("🚀 Iniciando servidor Django...")
    print("📍 API disponível em: http://127.0.0.1:8000/api/")
    print("🔧 Admin disponível em: http://127.0.0.1:8000/admin/")
    print("👤 Login admin: admin / admin123")
    print("\n⏹️  Para parar o servidor, pressione Ctrl+C")
    print("=" * 50)
    
    # Caminho para o Python do ambiente virtual
    python_path = os.path.join("venv", "Scripts", "python.exe")
    
    try:
        subprocess.run([python_path, "manage.py", "runserver"], check=True)
    except KeyboardInterrupt:
        print("\n🛑 Servidor interrompido pelo usuário")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao iniciar servidor: {e}")

if __name__ == "__main__":
    start_server()
