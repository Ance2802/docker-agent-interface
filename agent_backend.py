from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Configuration de l'IA avec la variable d'environnement (sécurité)
API_KEY = os.environ.get("GEMINI_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-3.5-flash')

@app.route('/api/ask', methods=['POST'])
def ask_agent():
    data = request.json
    question = data.get('question', '')
    
    if not API_KEY:
        return jsonify({"reponse": "Erreur : Clé API manquante."})
        
    try:
        # L'agent réfléchit avec Gemini
        response = model.generate_content(question)
        return jsonify({"reponse": response.text})
    except Exception as e:
        return jsonify({"reponse": f"Erreur : {str(e)}"})

@app.route('/')
def home():
    # On renvoie la page HTML
    with open('index.html', 'r', encoding='utf-8') as f:
        return f.read()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)