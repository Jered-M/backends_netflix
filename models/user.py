from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    """Modèle pour représenter un utilisateur"""
    
    users_db = []  # Simule une base de données
    
    def __init__(self, name, email, password):
        self.id = len(User.users_db) + 1
        self.name = name
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.created_at = datetime.now()
        self.favorites = []
        self.watch_history = []
    
    def check_password(self, password):
        """Vérifie si le mot de passe correspond"""
        return check_password_hash(self.password_hash, password)
    
    def add_to_favorites(self, media_id):
        """Ajoute un média aux favoris"""
        if media_id not in self.favorites:
            self.favorites.append(media_id)
    
    def remove_from_favorites(self, media_id):
        """Retire un média des favoris"""
        if media_id in self.favorites:
            self.favorites.remove(media_id)
    
    def add_to_history(self, media_id):
        """Ajoute un média à l'historique"""
        if media_id not in self.watch_history:
            self.watch_history.append(media_id)
    
    def to_dict(self):
        """Convertit l'objet en dictionnaire"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'favorites': self.favorites,
            'watch_history': self.watch_history,
            'created_at': self.created_at.isoformat()
        }
    
    @staticmethod
    def find_by_email(email):
        """Trouve un utilisateur par email"""
        for user in User.users_db:
            if user.email == email:
                return user
        return None
    
    @staticmethod
    def find_by_id(user_id):
        """Trouve un utilisateur par ID"""
        for user in User.users_db:
            if user.id == user_id:
                return user
        return None
    
    def save(self):
        """Sauvegarde l'utilisateur dans la base de données"""
        User.users_db.append(self)
        return self
