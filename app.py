from flask import Flask, render_template, request, redirect, url_for
import hashlib

app = Flask(__name__)

# Liste pour stocker les résultats
results = []

# Liste des algorithmes de hachage disponibles
HASH_ALGORITHMS = ['sha256', 'sha1', 'md5']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Récupérer la chaîne de caractères saisie par l'utilisateur
        input_str = request.form['input_str']
        
        # Récupérer l'algorithme choisi par l'utilisateur
        selected_algorithm = request.form.get('algorithm', 'sha256')
        
        # Calculer le checksum en utilisant l'algorithme sélectionné
        hash_value = hashlib.new(selected_algorithm, input_str.encode()).hexdigest()
        
        # Ajouter le résultat à la liste
        result = {
            'input': input_str,
            'algorithm': selected_algorithm,
            'hash': hash_value
        }
        results.append(result)
        
        # Rediriger vers la page d'accueil après la soumission
        return redirect(url_for('index'))

    return render_template('index.html', results=results, algorithms=HASH_ALGORITHMS)

if __name__ == '__main__':
    # Démarrer le serveur Flask
    app.run(host='0.0.0.0', port=5000)
