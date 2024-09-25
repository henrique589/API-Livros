# API-Livros

```cpp
#define AUTHOR ["Henrique Azevedo"]
```
&nbsp;

## Descrição do Projeto
API-Livros é uma API RESTful construída com Flask e SQLite para gerenciar uma coleção de livros. A API oferece endpoints para realizar operações CRUD (Criar, Ler, Atualizar, Deletar) em livros. A aplicação utiliza um banco de dados SQLite para armazenar os dados dos livros e pode ser facilmente expandida para usar outros bancos de dados.
&nbsp;

## URL base - localhost.com
&nbsp;

## Endpoints
- localhost/livros (GET)
- localhost/livros (POST)
- localhost/livros/id (GET)
- localhost/livros/id (PUT)
- localhost/livros (DELETE)
&nbsp;

## Dependências do Projeto
- Flask
- SQLite3
&nbsp;

## Como Executar o Projeto
1. Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/API-Livros.git
cd API-Livros
```

2. Criar o banco de dados
```bash
python src/database.py(.src/databse.py)
```

3. Executar o Servidor Flask
```bash
python src/app.py(.src/app.py)
```
&nbsp;
O script manage.py(.manage.py) foi criado para automatizar o processo de execução. Existe um guia no arquivo explicando como executar detalhadamente.