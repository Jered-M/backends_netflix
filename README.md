# Netflix Clone - Backend API

Backend Flask avec architecture MVC complète pour un clone de Netflix.

## 🎯 Architecture

Ce projet suit le pattern **MVC (Model-View-Controller)** avec une API REST :

```
backend/
├── models/              # Modèles de données
│   ├── user.py         # Gestion des utilisateurs
│   └── media.py        # Gestion des médias (films/séries)
├── controllers/         # Logique métier
│   ├── auth_controller.py    # Authentification
│   ├── media_controller.py   # Gestion des médias
│   └── user_controller.py    # Actions utilisateur
├── routes/              # Routes API
│   ├── auth_routes.py
│   ├── media_routes.py
│   └── user_routes.py
├── config/              # Configuration
│   └── config.py
├── app.py              # Point d'entrée de l'application
└── requirements.txt    # Dépendances Python
```

## 🚀 Installation

### Prérequis
- Python 3.8+
- pip

### Étapes

1. **Cloner le dépôt**
```bash
git clone https://github.com/Jered-M/backends_netflix.git
cd backends_netflix
```

2. **Créer un environnement virtuel**
```bash
python -m venv venv
```

3. **Activer l'environnement virtuel**
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

4. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

5. **Lancer le serveur**
```bash
python app.py
```

Le serveur sera accessible sur `http://localhost:5000`

## 📡 API Endpoints

### Authentification (`/api/auth`)

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| POST | `/api/auth/register` | Inscription d'un utilisateur |
| POST | `/api/auth/login` | Connexion |
| GET | `/api/auth/profile/:userId` | Récupérer le profil |

**Exemple de requête - Register:**
```json
POST /api/auth/register
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "password123"
}
```

### Médias (`/api`)

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| GET | `/api/trending` | Films et séries tendances |
| GET | `/api/films?query=Action&page=1` | Liste de films |
| GET | `/api/series?query=Drama&page=1` | Liste de séries |
| GET | `/api/media/:mediaId` | Détails d'un média |
| GET | `/api/search?q=query&type=movie` | Recherche |
| GET | `/api/genre?genre=Action&type=movie` | Médias par genre |

**Exemple de réponse - Trending:**
```json
{
  "films": [
    {
      "Title": "Inception",
      "Year": "2010",
      "imdbID": "tt1375666",
      "Type": "movie",
      "Poster": "https://..."
    }
  ],
  "series": [...]
}
```

### Utilisateur (`/api/user`)

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| GET | `/api/user/:userId/favorites` | Liste des favoris |
| POST | `/api/user/:userId/favorites` | Ajouter aux favoris |
| DELETE | `/api/user/:userId/favorites` | Retirer des favoris |
| GET | `/api/user/:userId/history` | Historique de visionnage |
| POST | `/api/user/:userId/history` | Ajouter à l'historique |

## 🔧 Technologies

- **Flask 3.0** - Framework web
- **Flask-CORS** - Gestion des CORS
- **Flask-WTF** - Gestion des formulaires
- **Requests** - Appels HTTP vers OMDb API
- **Werkzeug** - Sécurité et hashing

## 🎬 Source des données

Les données des films et séries proviennent de l'**API OMDb** (Open Movie Database).

Clé API configurée dans `config/config.py` :
```python
OMDB_API_KEY = '99673ad7'
```

## ⚙️ Configuration

Modifiez `config/config.py` pour personnaliser :
- Clé secrète Flask
- Clé API OMDb
- Origines CORS autorisées
- Mode debug

```python
class Config:
    SECRET_KEY = 'votre-clé-secrète'
    OMDB_API_KEY = 'votre-clé-omdb'
    CORS_ORIGINS = ['http://localhost:3000']
    DEBUG = True
```

## 📝 Modèles de données

### User
```python
{
    'id': int,
    'name': str,
    'email': str,
    'favorites': list,
    'watch_history': list,
    'created_at': datetime
}
```

### Media
```python
{
    'imdbID': str,
    'title': str,
    'year': str,
    'type': str,  # 'movie' ou 'series'
    'poster': str,
    'plot': str,
    'genre': str,
    'rating': str
}
```

## 🔒 Sécurité

- Mots de passe hashés avec **Werkzeug**
- CORS configuré pour origines spécifiques
- Validation des données avec **WTForms**

## 🚧 Limitations actuelles

- Base de données en mémoire (non persistante)
- Pas de JWT pour l'authentification
- Pas de rate limiting
- Mode debug activé

## 📈 Améliorations futures

- [ ] Intégrer PostgreSQL/MongoDB
- [ ] Authentification JWT
- [ ] Rate limiting
- [ ] Cache Redis
- [ ] Tests unitaires
- [ ] Documentation Swagger
- [ ] Docker
- [ ] CI/CD

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request.

## 📄 Licence

MIT

## 👤 Auteur

**Jered M**
- GitHub: [@Jered-M](https://github.com/Jered-M)

---

⭐ N'oubliez pas de mettre une étoile si ce projet vous a aidé !
