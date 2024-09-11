# libs
from flask import Flask, jsonify, request

# criação de uma aplicação Flask
app = Flask(__name__)

# Fonte de dados
livros = [
    {
        'id': 1,
        'título': 'O Senhos dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'título': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.k Howling'
    },
    {
        'id': 3,
        'título': 'Hábitos Atômicos',
        'autor': 'James Clear'
    },
]

# Consultar todos os livros da base
@app.route('/livros', methods=['GET'])
def obter_all():
    return jsonify(livros)

# Consultar livro por id
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

# Editar livro por id
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

# Criar um livro
@app.route('/livros', methods=['POST'])
def criar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

# Deletar um livro por id
@app.route('/livros/<int:id>', methods=['DELETE'])
def deletar_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)

app.run(port=5000, host='localhost', debug=True)