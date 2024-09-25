import os
import subprocess
import sys

# Função para executar um comando no terminal
def run_command(command):
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"Erro ao executar o comando: {command}")
        sys.exit(result.returncode)

def create_db():
    print("1. Criando o banco de dados e a tabela...")
    run_command("python src/database.py")

def populate_db():
    print("2. Populando o banco de dados com os dados do arquivo .txt...")
    run_command("python src/database.py")

def run_server():
    print("3. Iniciando o servidor Flask...")
    run_command("python src/app.py")

def clean_db():
    print("Removendo o arquivo de banco de dados...")
    db_path = os.path.join("src", "books.db")
    if os.path.exists(db_path):
        os.remove(db_path)
        print("Banco de dados removido.")
    else:
        print("Nenhum banco de dados encontrado.")

def show_help():
    print("""
Comandos disponíveis:
1. python manage.py db        -> Cria o banco de dados e a tabela
2. python manage.py populate  -> Popula o banco de dados com os dados do arquivo .txt
3. python manage.py run       -> Inicia o servidor Flask
4. python manage.py clean     -> Remove o arquivo de banco de dados
5. python manage.py start     -> Cria o banco de dados, popula e inicia o servidor Flask
    """)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        show_help()
    else:
        command = sys.argv[1]
        if command == 'db':
            create_db()
        elif command == 'populate':
            populate_db()
        elif command == 'run':
            run_server()
        elif command == 'clean':
            clean_db()
        elif command == 'start':
            create_db()
            populate_db()
            run_server()
        else:
            show_help()
