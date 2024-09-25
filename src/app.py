# libs
import os
from flask import Flask, jsonify, request
import json
import sqlite3

# criação de uma aplicação Flask
app = Flask(__name__)

# Conectando com o banco
def get_db_connection():
    conn = sqlite3.connect('books.db')
    # Retorna os resultados como um dicionário
    conn.row_factory = sqlite3.Row
    return conn

# Consultar todos os livros da base
@app.route('/livros', methods=['GET'])
def obter_all():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    livros = cursor.fetchall()
    conn.close()

    # Converter a lista em dicionario
    livros_disc = [dict(livro) for livro in livros]
    return jsonify(livros_disc)

# Consultar livro por id
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_id(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books WHERE id=?', (id,))
    livro = cursor.fetchone()
    conn.close()

    if livro:
        return jsonify(dict(livro))
    else:
        return jsonify({"error": "Livro não encontrado"}), 404


# Editar livro por id
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_id(id):
    livro_alterado = request.get_json()
    title = livro_alterado.get('title')
    author = livro_alterado.get('author')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books WHERE id=?', (id,))
    livro = cursor.fetchone()

    if livro:
        cursor.execute('UPDATE books SET title = ?, author = ? WHERE id = ?', (title, author, id))
        conn.commit()
        conn.close()
        return jsonify(livro_alterado)

# Criar um livro
@app.route('/livros', methods=['POST'])
def criar_livro():
    novo_livro = request.get_json()
    title = novo_livro.get('title')
    author = novo_livro.get('author')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books (title, author) VALUES (?, ?)', (title, author))
    conn.commit()
    livro_id = cursor.lastrowid
    conn.close()

    novo_livro['id'] = livro_id
    return jsonify(novo_livro), 201

# Deletar um livro por id
@app.route('/livros/<int:id>', methods=['DELETE'])
def deletar_livro(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books WHERE id=?', (id,))

    livro = cursor.fetchone()
    if livro:
        cursor.execute('DELETE FROM books WHERE id = ?', (id,))
        conn.commit()
        conn.close()
        return jsonify({"message": "Livro deletado com sucesso"})

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)