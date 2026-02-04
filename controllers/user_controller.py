from flask import jsonify, request
from models.user import User

class UserController:
    """Contrôleur pour gérer les actions utilisateur"""
    
    @staticmethod
    def add_to_favorites(user_id):
        """Ajoute un média aux favoris"""
        user = User.find_by_id(user_id)
        if not user:
            return jsonify({'error': 'Utilisateur non trouvé'}), 404
        
        data = request.get_json()
        media_id = data.get('mediaId')
        
        if not media_id:
            return jsonify({'error': 'ID du média manquant'}), 400
        
        user.add_to_favorites(media_id)
        return jsonify({
            'message': 'Ajouté aux favoris',
            'favorites': user.favorites
        }), 200
    
    @staticmethod
    def remove_from_favorites(user_id):
        """Retire un média des favoris"""
        user = User.find_by_id(user_id)
        if not user:
            return jsonify({'error': 'Utilisateur non trouvé'}), 404
        
        data = request.get_json()
        media_id = data.get('mediaId')
        
        if not media_id:
            return jsonify({'error': 'ID du média manquant'}), 400
        
        user.remove_from_favorites(media_id)
        return jsonify({
            'message': 'Retiré des favoris',
            'favorites': user.favorites
        }), 200
    
    @staticmethod
    def get_favorites(user_id):
        """Récupère les favoris d'un utilisateur"""
        user = User.find_by_id(user_id)
        if not user:
            return jsonify({'error': 'Utilisateur non trouvé'}), 404
        
        return jsonify({'favorites': user.favorites}), 200
    
    @staticmethod
    def add_to_history(user_id):
        """Ajoute un média à l'historique"""
        user = User.find_by_id(user_id)
        if not user:
            return jsonify({'error': 'Utilisateur non trouvé'}), 404
        
        data = request.get_json()
        media_id = data.get('mediaId')
        
        if not media_id:
            return jsonify({'error': 'ID du média manquant'}), 400
        
        user.add_to_history(media_id)
        return jsonify({
            'message': 'Ajouté à l\'historique',
            'history': user.watch_history
        }), 200
    
    @staticmethod
    def get_history(user_id):
        """Récupère l'historique d'un utilisateur"""
        user = User.find_by_id(user_id)
        if not user:
            return jsonify({'error': 'Utilisateur non trouvé'}), 404
        
        return jsonify({'history': user.watch_history}), 200
