from flask import Flask

# Créer une instance de l'application Flask
app = Flask(__name__)

# Définir une route pour la page d'accueil
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Exécuter l'application
if __name__ == '__main__':
    app.run(debug=True)
