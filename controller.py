from flask import Flask # Importa a biblioteca
from model import *

app = Flask(__name__) # Inicializa a aplicação

@app.route('/People', methods=["GET"]) # Cria uma rota
def getAllPeople():
    return Person.registrationOfPeople()

@app.route('/Person/<name>', methods=["GET"]) # Cria uma rota
def filterRecordByName(name):
    return Person.checkNameInSystem(name)

if __name__ == '__main__':
  app.run(debug=True) # Executa a aplicação