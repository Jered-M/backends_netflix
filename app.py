from flask import Flask, jsonify
from flask_cors import CORS
from config.config import Config
from routes.auth_routes import auth_bp
from routes.media_routes import media_bp
from routes.user_routes import user_bp

def create_app():
    """Factory pour créer l'application Flask"""
    
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Activer CORS pour permettre les requêtes depuis React
    CORS(app, resources={r"/api/*": {"origins": Config.CORS_ORIGINS}})
    
    # Enregistrer les blueprints (routes)
    app.register_blueprint(auth_bp)
    app.register_blueprint(media_bp)
    app.register_blueprint(user_bp)
    
    # Route de base pour vérifier que l'API fonctionne
    @app.route('/')
    def index():
        return jsonify({
            'message': 'Bienvenue sur l\'API Netflix Clone',
            'version': '1.0',
            'endpoints': {
                'auth': '/api/auth',
                'media': '/api',
                'user': '/api/user'
            }
        })
    
    # Gestion des erreurs 404
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Route non trouvée'}), 404
    
    # Gestion des erreurs 500
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'error': 'Erreur serveur interne'}), 500
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
