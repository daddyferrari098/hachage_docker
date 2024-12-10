# Utiliser l'image de base Python
FROM python:3.9-slim

# lerépertoire de travail
WORKDIR /app

# Copie les fichiers de l'application
COPY . .

# Installe les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Définition de la commande de démarrage
CMD ["python", "app.py"]
