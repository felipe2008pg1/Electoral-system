from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
ARQUIVO_JSON = "votos.json"

def carregar_dados():
    if not os.path.exists(ARQUIVO_JSON):
        dados_padrao = [
            {"candidato": "FELIPE", "votos": 0},
            {"candidato": "GONZALEZ", "votos": 0}
        ]
        with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
            json.dump(dados_padrao, f, indent=4, ensure_ascii=False)
        return dados_padrao
    with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_dados(dados):
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


@app.route('/')
def index():
    candidatos = carregar_dados()
    return render_template('index.html', candidatos=candidatos)


@app.route('/votar', methods=['POST'])
def votar():
    nome_candidato = request.form.get('candidato')
    candidatos = carregar_dados()
    
    for c in candidatos:
        if c['candidato'] == nome_candidato:
            c['votos'] += 1
            break
            
    salvar_dados(candidatos)
    return redirect(url_for('index')) 

if __name__ == '__main__':
    app.run(debug=True)
