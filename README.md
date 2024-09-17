

# Orange County Lettings

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
