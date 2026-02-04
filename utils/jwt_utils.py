import jwt
import datetime
from functools import wraps
from flask import request, jsonify
from config.config import Config

def generate_token(user_id):
    """Générer un token JWT pour l'utilisateur"""
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),  # Expire dans 7 jours
        'iat': datetime.datetime.utcnow()
    }
    
    token = jwt.encode(payload, Config.SECRET_KEY, algorithm='HS256')
    return token

def decode_token(token):
    """Décoder et vérifier un token JWT"""
    try:
        payload = jwt.decode(token, Config.SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None  # Token expiré
    except jwt.InvalidTokenError:
        return None  # Token invalide

def token_required(f):
    """Décorateur pour protéger les routes qui nécessitent une authentification"""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        # Récupérer le token depuis le header Authorization
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            try:
                token = auth_header.split(' ')[1]  # Format: "Bearer TOKEN"
            except IndexError:
                return jsonify({'error': 'Format du token invalide'}), 401
        
        if not token:
            return jsonify({'error': 'Token manquant'}), 401
        
        # Vérifier le token
        payload = decode_token(token)
        if not payload:
            return jsonify({'error': 'Token invalide ou expiré'}), 401
        
        # Passer l'ID utilisateur à la fonction
        return f(user_id=payload['user_id'], *args, **kwargs)
    
    return decorated
