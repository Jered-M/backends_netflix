from flask import jsonify, request
from models.user import User
from utils.jwt_utils import generate_token, token_required

class AuthController:
    """Contrôleur pour gérer l'authentification"""
    
    @staticmethod
    def register():
        """Inscription d'un nouvel utilisateur"""
        data = request.get_json()
        
        # Validation des données
        if not data or not data.get('name') or not data.get('email') or not data.get('password'):
            return jsonify({'error': 'Données manquantes'}), 400
        
        # Vérifier si l'email existe déjà
        if User.find_by_email(data['email']):
            return jsonify({'error': 'Cet email est déjà utilisé'}), 400
        
        # Créer et sauvegarder l'utilisateur
        user = User(
            name=data['name'],
            email=data['email'],
            password=data['password']
        )
        user.save()
        
        # Générer le token JWT
        token = generate_token(user.id)
        
        return jsonify({
            'message': 'Inscription réussie',
            'user': user.to_dict(),
            'token': token
        }), 201
    
    @staticmethod
    def login():
        """Connexion d'un utilisateur"""
        data = request.get_json()
        
        # Validation des données
        if not data or not data.get('email') or not data.get('password'):
            return jsonify({'error': 'Email et mot de passe requis'}), 400
        
        # Trouver l'utilisateur
        user = User.find_by_email(data['email'])
        
        if not user or not user.check_password(data['password']):
            return jsonify({'error': 'Email ou mot de passe incorrect'}), 401
        
        # Générer le token JWT
        token = generate_token(user.id)
        
        return jsonify({
            'message': 'Connexion réussie',
            'user': user.to_dict(),
            'token': token
        }), 200
    
    @staticmethod
    @token_required
    def get_profile(user_id):
        """Récupérer le profil d'un utilisateur"""
        user = User.find_by_id(user_id)
        
        if not user:
            return jsonify({'error': 'Utilisateur non trouvé'}), 404
        
        return jsonify(user.to_dict()), 200
