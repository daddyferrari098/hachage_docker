# Calculateur de Checksum avec Flask et Redis

Ce projet est une application Flask qui permet de calculer les valeurs de hachage (checksum) d'une chaîne de caractères entrée par l'utilisateur, en utilisant différents algorithmes de hachage tels que SHA-256, SHA-1 et MD5. Les résultats sont stockés dans une base de données Redis pour une gestion efficace des données. L'application utilise Docker pour simplifier l'exécution et la gestion des dépendances.

## Prérequis
- Docker et Docker-compose
- Redis

## Cloner le dépôt
Vous cloner le depot

## Construire et démarrer les containers
docker-compose up --build

## Acceder à l'apllication
http://localhost:5000

## Structure du projet

/App-laye
├── Dockerfile           # Dockerfile pour construire l'image du conteneur Flask
├── docker-compose.yml   # Configuration Docker Compose
├── app.py               # Code principal de l'application Flask
├── requirements.txt     # Liste des dépendances Python  
└── templates/
    └── index.html       # Template HTML pour l'interface utilisateur
    └──style.css         # Pour mettre un peu de style 


## Le Dockerfile 
contient les instructions pour construire l'image Docker de l'application Flask. Il commence par une image de base Python, puis copie les fichiers nécessaires, installe les dépendances Python, et spécifie la commande pour démarrer l'application Flask

## le docker-compose.yml
Configure Docker Compose pour exécuter l'application Flask dans un conteneur et Redis dans un autre. Il lie le port 5000 du conteneur Flask au port 5000 de l'hôte, ce qui me permet d'accéder à l'application depuis le navigateur.

## Redis 

Vous pouvez voir les données en utilisant redis-cli 
