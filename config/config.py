import os

class Config:
    """Configuration de l'application"""
    
    # Clé secrète pour Flask
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'jered-netflix-clone-secret-key'
    
    # Clé API OMDb
    OMDB_API_KEY = os.environ.get('OMDB_API_KEY') or '99673ad7'
    
    # CORS
    CORS_ORIGINS = ['http://localhost:3000', 'http://127.0.0.1:3000']
    
    # Debug
    DEBUG = True
