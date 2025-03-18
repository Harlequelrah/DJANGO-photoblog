# PhotoBlog

**PhotoBlog** est un blog de photos développé avec **Django**. Il permet à certains utilisateurs de publier des photos, tandis que d'autres peuvent simplement visualiser les photos partagées. Ce projet intègre une fonctionnalité d'authentification pour différencier les utilisateurs qui peuvent publier et ceux qui peuvent seulement visualiser les photos.

## Fonctionnalités

- **Authentification des utilisateurs** : Inscription, connexion, et gestion des comptes utilisateurs.
- **Publication de photos** : Les utilisateurs ayant un rôle spécifique (par exemple, "contributeur") peuvent publier des photos.
- **Vue des photos** : Les utilisateurs peuvent visualiser les photos publiées sur le blog.
- **Rôles d'utilisateurs** : Des rôles distincts pour les utilisateurs peuvent être gérés (par exemple, "lecteur" et "contributeur").

## Technologies utilisées

- **Python 3.x** 
- **Django** (version x.x)
- **MySQL** (base de données par défaut, peut être configurée pour d'autres SGBD)

## Installation

### Prérequis
- **Python** version 3.x installé sur votre machine.
- **Pip** pour gérer les dépendances Python.

### Étapes d'installation

1. **Cloner le projet** :

    ```bash
    git clone https://github.com/Harlequelrah/DJANGO-photoblog
    cd photoblog
    ```

2. **Créer un environnement virtuel** :

    ```bash
    python -m venv venv
    source venv/bin/activate  # Sous Linux/Mac
    venv\Scripts\activate  # Sous Windows
    ```

3. **Installer les dépendances** :

    ```bash
    pip install -r requirements.txt
    ```

4. **Configurer la base de données** :

    Vous pouvez simplement exécuter :

    ```bash
    python manage.py migrate
    ```

    Si vous préférez un autre SGBD, vous devrez configurer les paramètres de connexion à la base de données dans le fichier `settings.py`.

5. **Créer un super utilisateur (facultatif, pour accéder au backoffice)** :

    ```bash
    python manage.py createsuperuser
    ```

6. **Démarrer le serveur de développement** :

    ```bash
    python manage.py runserver
    ```

    Vous pouvez maintenant accéder à l'application à l'adresse suivante : [http://127.0.0.1:8000](http://127.0.0.1:8000)

