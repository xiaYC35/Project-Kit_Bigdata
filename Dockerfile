# Environnement de fonctionnement du programme
FROM python:3.10
# Mise en place d'un répertoire de travail à l'intérieur d'un conteneur Docker
WORKDIR /app
# Copier le requirements.txt dans le répertoire de travail 
COPY requirements.txt /app
# Installer les dépendances nécessaires
RUN pip install -r requirements.txt
# Copier des fichiers locaux dans une image Docker
COPY . /app
# Définir les commandes à exécuter au démarrage du conteneur
CMD ["python", "app.py"]

# Exécution d'une application dans un seul conteneur, sans nécessité de coordination avec d'autres conteneurs, donc pas besoin de Docker Compose.
# docker build -t todolistimage .
# docker run -p <host_port>:<container_port> -d todolistimage
