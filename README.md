

# Orange County Lettings

**URL :**

Documentation technique :

https://orange-county-lettings-documentation-lg.readthedocs.io/fr/latest/index.html

Repo documentation :

https://github.com/El-GuiGui/Orange-County-Lettings-Documentation-LG


## Résumé
Orange County Lettings est un site web permettant de gérer des profils et des locations. Cette documentation couvre la configuration pour le développement local, le linting, les tests unitaires, et l'interaction avec la base de données et le panneau d'administration.

## Prérequis
- Compte GitHub avec accès en lecture au repository du projet.
- Git CLI
- SQLite3 CLI
- Python (version 3.6 ou supérieure)


## Développement Local


#### 1. Cloner le Repository
```bash
cd /path/to/put/project/in
```
```bash
git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git
```

#### 2. Créer un Environnement Virtuel
```bash
cd /path/to/Python-OC-Lettings-FR
```
```bash
python -m venv venv
```

#### 3. Activer l'Environnement Virtuel
```bash
source venv/bin/activate
```

#### 4. Vérifications
- Confirmez que `python` pointe vers l'interpréteur de l'environnement virtuel:
  ```bash
  which python
  ```
- Assurez-vous que la version de Python est 3.6 ou supérieure:
  ```bash
  python --version
  ```
- Vérifiez que `pip` pointe vers l'exécutable de l'environnement virtuel:
  ```bash
  which pip
  ```

*Pour désactiver l'environnement virtuel:*
```bash
deactivate
```

#### 5. Exécuter le Site Web
```bash
cd /path/to/Python-OC-Lettings-FR
```
```bash
source venv/bin/activate
```
```bash
pip install --requirement requirements.txt
```
```bash
python manage.py runserver
```
Ouvrez [http://localhost:8000](http://localhost:8000) dans un navigateur pour confirmer que le site fonctionne et qu'il est possible de naviguer à travers les profils et les locations.

Pensez à modifier le DEBUG MODE a "True" dans le settings.py de l'app principale pour utiliser l'environnement local sans avoir de soucis avec les fichiers statics ...
## Linting
Pour vérifier la qualité du code avec Flake8:
```bash
cd /path/to/Python-OC-Lettings-FR
```
```bash
source venv/bin/activate
```
```bash
flake8
```

## Tests Unitaires
Pour exécuter les tests unitaires:
```bash
cd /path/to/Python-OC-Lettings-FR
```
```bash
source venv/bin/activate
```
```bash
pytest
```

## Interagir avec la Base de Données
```bash
cd /path/to/Python-OC-Lettings-FR
sqlite3
```
- Connectez-vous à la base de données:
  ```bash
  .open oc-lettings-site.sqlite3
  ```
- Affichez les tables:
  ```bash
  .tables
  ```
- Affichez les colonnes dans la table des profils:
  ```bash
  pragma table_info(Python-OC-Lettings-FR_profile);
  ```
- Effectuez une requête sur la table des profils:
  ```bash
  select user_id, favorite_city from Python-OC-Lettings-FR_profile where favorite_city like 'B%';
  ```
- Quittez SQLite:
  ```bash
  .quit
  ```

## Accéder au Panneau d'Administration
Ouvrez [http://localhost:8000/admin](http://localhost:8000/admin) et connectez-vous avec les identifiants:
- **Utilisateur**: `admin`
- **Mot de passe**: `Abc1234!`


## Déploiement et utilisation 

Pour un usage en production avec un Debug a False pensez au :
  ```bash
  python manage.py collectstatic
  ```

et à la configuration du serveur pour l'utilisation des statics.


On peut éventuellement utilisé :
  ```bash
  python manage.py runserver --insecure
  ```





## Déploiement

Le déploiement de ce projet se fait en suivant un pipeline CI/CD via GitHub Actions. Le processus garantit que les tests, le linting, et la conteneurisation de l'application sont effectués correctement avant tout déploiement en production. 

Le site est ensuite déployé sur la plateforme Render en utilisant l'image Docker générée.

### Prérequis

- Un compte sur [Docker Hub](https://hub.docker.com/).
- Un compte sur [Render](https://render.com/).
- Les variables d'environnement configurées dans GitHub Secrets (ex : `DOCKER_USERNAME`, `DOCKER_PASSWORD`, `RENDER_API_KEY`, `RENDER_DEPLOY_HOOK`, `SENTRY_DSN`, `SECRET_KEY`, etc.).
- L'application est configurée pour fonctionner avec les fichiers statiques et le service de gestion des erreurs Sentry.

### Pipeline CI/CD

Le déploiement est automatisé grâce à un fichier `config.yml` dans le répertoire `.github/workflows/` qui déclenche un ensemble de jobs à chaque push sur la branche `main` :

1. **Tests et Linting :** Le pipeline commence par exécuter un ensemble de tests unitaires et un linting avec flake8. Si cette étape échoue, le processus de déploiement est arrêté.
2. **Build et Push Docker :** Si les tests réussissent, l'image Docker de l'application est construite avec un tag correspondant au hash du commit (`github.sha`) et est ensuite poussée sur Docker Hub. Une image `latest` est également poussée à chaque mise à jour.
3. **Déploiement sur Render :** Après que l'image Docker est poussée, un hook de déploiement est déclenché pour Render, spécifiant l'URL de l'image Docker à utiliser pour le déploiement en production.

### Déploiement manuel local

Pour tester localement en utilisant l'image Docker, vous pouvez exécuter les commandes suivantes :

1. **Récupérer l'image Docker depuis Docker Hub :**
   ```bash
   docker pull ggui/oc_lettings:latest


2. **Lancer l'image et accèder au site :**

   ```bash
   docker run -d -p 8000:8000 ggui/oc_lettings:latest


3. **Accéder à l'application :**

Ouvrez [http://localhost:8000](http://localhost:8000) dans votre navigateur pour voir l'application fonctionner en local.

### Variables d'environnement

Les secrets et variables sensibles ne doivent jamais être stockés en dur dans le code source. GitHub Secrets et les variables d'environnement sont utilisés pour sécuriser les informations sensibles telles que :

- `SECRET_KEY`: La clé secrète Django.
- `SENTRY_DSN`: Le DSN pour la surveillance des erreurs via Sentry.
- `DOCKER_USERNAME` et `DOCKER_PASSWORD`: Pour la connexion à Docker Hub.
- `RENDER_API_KEY` et `RENDER_DEPLOY_HOOK`: Utilisés pour déclencher le déploiement sur Render.

### Suivi des erreurs et gestion des fichiers statiques

- **Sentry** : Utilisé pour suivre les erreurs en temps réel pendant et après le déploiement. Les erreurs capturées apparaîtront dans votre tableau de bord Sentry.
- **Whitenoise** : Utilisé pour gérer les fichiers statiques dans l'environnement de production. Configuré  dans le fichier `settings.py`.

### Automatisation du déploiement

Le déploiement est entièrement automatisé via le pipeline CI/CD, garantissant que chaque modification poussée sur la branche `main` entraîne :

- Un cycle complet de tests et de linting.
- La génération et le déploiement d'une image Docker à jour.
- Le déploiement automatique sur Render, rendant l'application accessible publiquement.

En cas d'échec à une quelconque étape du processus, le déploiement est **annulé**, et l'image Docker n'est ni poussée ni déployée.

