import sqlite3
import json
import os

# Função para conectar ao banco de dados e criar a tabela
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL
            )
        ''')
        conn.commit()
        print("Tabela 'books' criada com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    finally:
        if conn:
            conn.close()

# Função para popular o banco de dados com dados de um arquivo .txt
def popular_banco_de_dados():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()

    # Obter o caminho do arquivo .txt
    caminho_arquivo = os.path.abspath('data/books.txt')

    # Ler os dados do arquivo .txt
    with open(caminho_arquivo, 'r', encoding='utf-8') as file:
        books = json.load(file)

    # Inserir os dados no banco de dados
    for book in books:
        cursor.execute('INSERT INTO books (title, author) VALUES (?, ?)', (book['título'], book['autor']))

    conn.commit()
    conn.close()
    print(f"{len(books)} livros inseridos no banco de dados.")

if __name__ == '__main__':
    create_connection()
    popular_banco_de_dados()
