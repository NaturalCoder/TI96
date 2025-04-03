from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)

# Simular um banco de dados com um arquivo JSON 
ARQUIVO_DB = 'tarefas.json'

def carregar_tarefas():
    try:
        with open(ARQUIVO_DB, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO_DB, 'w') as arquivo:
        json.dump(tarefas, arquivo)

def calcular_tempo_restante(data_final):
    if not data_final:
        return None
    hoje = datetime.now()
    data_fim = datetime.strptime(data_final, '%Y-%m-%d')
    diferenca = data_fim - hoje
    if diferenca.days < 0:
        return "Atrasada"
    return f"{diferenca.days} dias restantes"

@app.route('/tarefas', methods=['GET'])
def obter_tarefas():
    tarefas = carregar_tarefas()
    for tarefa in tarefas:
        tarefa['tempo_restante'] = calcular_tempo_restante(tarefa.get('data_final'))
    return jsonify(tarefas)

@app.route('/tarefas', methods=['POST'])
def adicionar_tarefa():
    tarefa = request.json
    # Adiciona campos de data e status
    tarefa['data_final'] = tarefa.get('data_final', '')
    tarefa['concluida'] = tarefa.get('concluida', False)
    tarefa['tempo_restante'] = calcular_tempo_restante(tarefa['data_final'])
    tarefas = carregar_tarefas()
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    return jsonify(tarefa), 201

@app.route('/tarefas/<int:id>', methods=['PUT'])
def atualizar_tarefa(id):
    tarefas = carregar_tarefas()
    tarefa = request.json
    
    for i, t in enumerate(tarefas):
        if t['id'] == id:
            tarefas[i] = tarefa
            salvar_tarefas(tarefas)
            return jsonify(tarefa)
    
    return jsonify({'erro': 'Tarefa não encontrada'}), 404

@app.route('/tarefas/<int:id>', methods=['DELETE'])
def deletar_tarefa(id):
    tarefas = carregar_tarefas()
    
    for i, tarefa in enumerate(tarefas):
        if tarefa['id'] == id:
            tarefas.pop(i)
            salvar_tarefas(tarefas)
            return jsonify({'mensagem': 'Tarefa removida com sucesso'})
    
    return jsonify({'erro': 'Tarefa não encontrada'}), 404

@app.route('/tarefas/atrasadas', methods=['GET'])
def verificar_tarefas_atrasadas():
    tarefas = carregar_tarefas()
    hoje = datetime.now()
    tarefas_atrasadas = []
    
    for tarefa in tarefas:
        if not tarefa['concluida'] and tarefa['data_final']:
            data_final = datetime.strptime(tarefa['data_final'], '%Y-%m-%d')
            if data_final < hoje:
                tarefa['atrasada'] = True
                tarefas_atrasadas.append(tarefa)
    
    return jsonify(tarefas_atrasadas)

if __name__ == '__main__':
    app.run(debug=True)
