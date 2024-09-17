from flask import Flask, jsonify, request

app = Flask(__name__)

personagensJJK = [
    {
        'id' : 1,
        'nome': 'Satoru Gojo'
    },
    
    {
        'id' : 2,
        'nome': 'Yuji Itadori'
    }
       
]

@app.route('/personagens', methods=['GET'])
def obter_personagens():
    return jsonify(personagensJJK)

@app.route('/personagens/<int:id>', methods=['GET'])
def obter_personagem_id(id):
    for personagen in personagensJJK:
       if personagen.get('id') == id:
           return jsonify(personagen)

app.run(port=5000, host='localhost', debug=True)