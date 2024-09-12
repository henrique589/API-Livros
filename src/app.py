# libs
import os
from flask import Flask, jsonify, request
import json

# criação de uma aplicação Flask
app = Flask(__name__)

# Obtendo o caminho do arquivo de dados
def caminho_dados():
    return os.path.abspath('data/books.txt')

# Leitura dos dados do arquivo
def leitura_dados():
    try:
        with open(caminho_dados(), 'r', encoding='utf-8') as file:
            books = json.load(file)
    except FileNotFoundError:
        books = []
    return books 

# Escrita no arquivo de dados
def escrever_dados(books):
    with open(caminho_dados(), 'w', encoding='utf-8') as file:
        json.dump(books, file, ensure_ascii=False, indent=4)

# Consultar todos os livros da base
@app.route('/livros', methods=['GET'])
def obter_all():
    livros = leitura_dados()
    return jsonify(livros)

# Consultar livro por id
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_id(id):
    livros = leitura_dados()
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

# Editar livro por id
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_id(id):
    livros = leitura_dados()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livro_alterado = request.get_json()
            livros[indice].update(livro_alterado)
            escrever_dados(livros)
            return jsonify(livros[indice])

# Criar um livro
@app.route('/livros', methods=['POST'])
def criar_livro():
    livros = leitura_dados()
    novo_livro = request.get_json()
    novo_livro['id'] = len(livros) + 1
    livros.append(novo_livro)
    escrever_dados(livros)
    return jsonify(novo_livro)

# Deletar um livro por id
@app.route('/livros/<int:id>', methods=['DELETE'])
def deletar_livro(id):
    livros = leitura_dados()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    escrever_dados(livros)
    return jsonify(livro)

app.run(port=5000, host='localhost', debug=True)