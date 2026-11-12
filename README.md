# 🐳 Agent IA Conteneurisé (Docker + Flask)

## Description
Une application web complète où l'utilisateur peut discuter avec une IA (Gemini). L'application est entièrement conteneurisée avec Docker pour garantir sa portabilité.

## Stack Technique
- **Backend** : Python (Flask).
- **Frontend** : HTML/CSS/JavaScript.
- **IA** : Google Gemini API.
- **Déploiement** : Docker.

## Comment lancer le projet
1. Cloner le dépôt.
2. Construire l'image : `docker build -t mon-agent .`
3. Lancer le conteneur : `docker run -p 5000:5000 -e GEMINI_API_KEY="VOTRE_CLE" mon-agent`
4. Ouvrir `http://localhost:5000`.