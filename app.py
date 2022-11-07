from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id' : 1,
        'descricao': 'o poder do amanha',
        'dataCriacao' : '10-10-2002'
    },
    {
        'id' : 2,
        'descricao': '5 habitos para o sucesso',
        'dataCriacao' : '02-05-2002'
    },
    {
        'id' : 3,
        'descricao': 'o tempo em sua mao',
        'dataCriacao' : '01-09-2002'
    },
]

#buscar itens
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)


#buscar item por id
@app.route('/livros/<int:id>', methods=['GET'])
def obter_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
    
#Editar item por id
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
            

#Adicionar livro
@app.route('/livros', methods=['POST'])
def adicionar_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)     
    
app.run(host='localhost',debug=True)
