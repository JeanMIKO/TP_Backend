🎓 Système de gestion des étudiants et de leurs
maîtres de mémoire 

 Contexte et objectif
La gestion des étudiants et de leurs maîtres de mémoire est un processus essentiel dans les établissements d’enseignement supérieur.  
Ce projet vise à automatiser le processus d’attribution de maîtres de mémoire et à fournir une API sécurisée pour :  

- Les  administrateurs: gestion des étudiants, enseignants et attributions.  
- Les enseignants : consultation de leurs étudiants attribués et notation.  
- Les étudiants : visualisation de leur maître de mémoire, mise à jour de leur thème, et accès à leurs notes.  

Cette API RESTful est développée avec Django et Django REST Framework, avec authentification JWT.  


🚀 Fonctionnalités

- ✅ Authentification & gestion des rôles utilisateurs (Admin, Étudiant, Enseignant).  
- ✅ Enregistrement et gestion des étudiants.  
- ✅ Enregistrement et gestion des enseignants.  
- ✅ Attribution d’un maître de mémoire (enseignant) à un étudiant selon son thème et la spécialité.  
- ✅ Notation des étudiants par leur maître de mémoire.  
- ✅ Consultation des attributions et des notes.  


 Rôles utilisateurs

Administrateur
- Gérer les étudiants et enseignants.  
- Attribuer un maître de mémoire à un étudiant.  
- Consulter toutes les notes et attributions.  

Enseignant
- Consulter la liste de ses étudiants attribués.  
- Attribuer une note à un étudiant.  

 Étudiant
- Mettre à jour son thème mémoire.  
- Consulter son maître de mémoire attribué.  
- Consulter ses notes.  


 Technologies utilisées
- Python 3.12.3
- Django 5.
- Django REST Framework
- [SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/)  
- [PostgreSQL](https://www.postgresql.org/) (production)

📂 Structure du projet

Gestion_app/
│── Gestion_app/ # Configuration principale (settings, urls, wsgi)
│── app_gestion/ # Application métier
│ ├── models/ # Modèles : Utilisateur, Étudiant, Enseignant, Attribution, Note
│ ├── serializers/ 
│ ├── views/
│ ├── permissions.py # Permissions custom (Admin, Enseignant, Étudiant)
│ └── routes.py # Routes de l'app
│
│── manage.py
│── requirements.txt
│── .env # variables d’environnement
│── .gitignore # Fichiers ignorés par Git
│── README.md # Documentation


⚙️ Installation et configuration

 1️⃣ Cloner le projet
git clone https://github.com/JeanMIKO/TP_Backend.git
cd  TP_Backend

2️⃣ Créer un environnement virtuel
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

3️⃣ Installer les dépendances
pip install -r requirements.txt

4️⃣ Configurer les variables d’environnement


⚠️ Important : .env et db.sqlite3 sont ignorés grâce à .gitignore pour ne pas exposer de données sensibles.

5️⃣ Lancer les migrations
python manage.py migrate


6️⃣ Démarrer le serveur

python manage.py runserver




📌 Endpoints principaux
🔹 Utilisateurs
POST /api/register/ → créer un utilisateur.

🔹 Étudiants
GET /api/etudiants/ → liste des étudiants (admin).

PATCH /api/etudiants/<id>/theme/ → modifier son thème mémoire (étudiant).

GET /api/etudiants/<id>/notes/ → consulter ses notes.

GET /api/etudiants/<id>/advisor/ → voir son maître de mémoire.

🔹 Enseignants
GET /api/enseignants/ → liste des enseignants (admin).

GET /api/enseignants/<id>/students/ → voir ses étudiants attribués (enseignant).

POST /api/enseignants/<id>/note-student/ → attribuer une note à un étudiant (enseignant).

🔹 Attributions
GET /api/attributions/ → liste des attributions (admin).

POST /api/attributions/ → attribuer un enseignant à un étudiant (admin).

🔹 Notes
GET /api/notes/ → voir toutes les notes (admin ou enseignant).

🗄️ Modèle de données (simplifié)
Utilisateur (username, email, rôle)

Étudiant (lié à un utilisateur, thème mémoire)

Enseignant (lié à un utilisateur, spécialité)

Attribution (un enseignant ↔ un étudiant, date d’attribution)

Note (valeur, commentaire, étudiant, enseignant)

✅ Bonnes pratiques
Toujours créer un fichier .env local et ne jamais l’exposer.

Tester les endpoints avec Postman ou cURL.

Protéger les routes avec JWT et respecter les permissions (Admin, Étudiant, Enseignant).🎓 Système de gestion des étudiants et de leurs
maîtres de mémoire 

 Contexte et objectif
La gestion des étudiants et de leurs maîtres de mémoire est un processus essentiel dans les établissements d’enseignement supérieur.  
Ce projet vise à automatiser le processus d’attribution de maîtres de mémoire et à fournir une API sécurisée pour :  

- Les  administrateurs: gestion des étudiants, enseignants et attributions.  
- Les enseignants : consultation de leurs étudiants attribués et notation.  
- Les étudiants : visualisation de leur maître de mémoire, mise à jour de leur thème, et accès à leurs notes.  

Cette API RESTful est développée avec Django et Django REST Framework, avec authentification JWT.  


🚀 Fonctionnalités

- ✅ Authentification & gestion des rôles utilisateurs (Admin, Étudiant, Enseignant).  
- ✅ Enregistrement et gestion des étudiants.  
- ✅ Enregistrement et gestion des enseignants.  
- ✅ Attribution d’un maître de mémoire (enseignant) à un étudiant selon son thème et la spécialité.  
- ✅ Notation des étudiants par leur maître de mémoire.  
- ✅ Consultation des attributions et des notes.  


 Rôles utilisateurs

Administrateur
- Gérer les étudiants et enseignants.  
- Attribuer un maître de mémoire à un étudiant.  
- Consulter toutes les notes et attributions.  

Enseignant
- Consulter la liste de ses étudiants attribués.  
- Attribuer une note à un étudiant.  

 Étudiant
- Mettre à jour son thème mémoire.  
- Consulter son maître de mémoire attribué.  
- Consulter ses notes.  


 Technologies utilisées
- Python 3.12.3
- Django 5.
- Django REST Framework
- [SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/)  
- [PostgreSQL](https://www.postgresql.org/) (production)

📂 Structure du projet

Gestion_app/
│── Gestion_app/ # Configuration principale (settings, urls, wsgi)
│── app_gestion/ # Application métier
│ ├── models/ # Modèles : Utilisateur, Étudiant, Enseignant, Attribution, Note
│ ├── serializers/ 
│ ├── views/
│ ├── permissions.py # Permissions custom (Admin, Enseignant, Étudiant)
│ └── routes.py # Routes de l'app
│
│── manage.py
│── requirements.txt
│── .env # variables d’environnement
│── .gitignore # Fichiers ignorés par Git
│── README.md # Documentation


⚙️ Installation et configuration

 1️⃣ Cloner le projet
git clone https://github.com/JeanMIKO/TP_Backend.git
cd  TP_Backend

2️⃣ Créer un environnement virtuel
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

3️⃣ Installer les dépendances
pip install -r requirements.txt

4️⃣ Configurer les variables d’environnement


⚠️ Important : .env et db.sqlite3 sont ignorés grâce à .gitignore pour ne pas exposer de données sensibles.

5️⃣ Lancer les migrations
python manage.py migrate


6️⃣ Démarrer le serveur

python manage.py runserver




📌 Endpoints principaux
🔹 Utilisateurs
POST /api/register/ → créer un utilisateur.

🔹 Étudiants
GET /api/etudiants/ → liste des étudiants (admin).

PATCH /api/etudiants/<id>/theme/ → modifier son thème mémoire (étudiant).

GET /api/etudiants/<id>/notes/ → consulter ses notes.

GET /api/etudiants/<id>/advisor/ → voir son maître de mémoire.

🔹 Enseignants
GET /api/enseignants/ → liste des enseignants (admin).

GET /api/enseignants/<id>/students/ → voir ses étudiants attribués (enseignant).

POST /api/enseignants/<id>/note-student/ → attribuer une note à un étudiant (enseignant).

🔹 Attributions
GET /api/attributions/ → liste des attributions (admin).

POST /api/attributions/ → attribuer un enseignant à un étudiant (admin).

🔹 Notes
GET /api/notes/ → voir toutes les notes (admin ou enseignant).

🗄️ Modèle de données (simplifié)
Utilisateur (username, email, rôle)

Étudiant (lié à un utilisateur, thème mémoire)

Enseignant (lié à un utilisateur, spécialité)

Attribution (un enseignant ↔ un étudiant, date d’attribution)

Note (valeur, commentaire, étudiant, enseignant)

✅ Bonnes pratiques
Toujours créer un fichier .env local et ne jamais l’exposer.

Tester les endpoints avec Postman ou cURL.

Protéger les routes avec JWT et respecter les permissions (Admin, Étudiant, Enseignant).