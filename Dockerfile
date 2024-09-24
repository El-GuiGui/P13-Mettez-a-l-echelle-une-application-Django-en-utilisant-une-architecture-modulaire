# Utiliser l'image de base python:3.9-alpine
FROM python:3.9-alpine

# Définir le répertoire de travail dans le conteneur
WORKDIR /

# Copier le fichier des dépendances dans le conteneur
COPY requirements.txt /

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le reste du projet dans le conteneur
COPY . /

# Collecter les fichiers statiques (CSS, JS)
RUN python manage.py collectstatic --noinput && gunicorn oc_lettings_site.wsgi



# Exposer le port 8000 pour accéder à l'application
EXPOSE 8000

# Commande pour démarrer l'application Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
