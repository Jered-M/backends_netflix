import requests
from flask import jsonify, request
from config.config import Config
from models.media import Media

class MediaController:
    """Contrôleur pour gérer les films et séries"""
    
    @staticmethod
    def get_trending():
        """Récupère les films et séries tendances"""
        # Films populaires
        films_response = requests.get(
            f"http://www.omdbapi.com/?s=Marvel&apikey={Config.OMDB_API_KEY}"
        ).json()
        
        # Séries populaires
        series_response = requests.get(
            f"http://www.omdbapi.com/?s=Game&type=series&apikey={Config.OMDB_API_KEY}"
        ).json()
        
        films = films_response.get('Search', [])[:10] if films_response.get('Response') == 'True' else []
        series = series_response.get('Search', [])[:10] if series_response.get('Response') == 'True' else []
        
        return jsonify({
            'films': films,
            'series': series
        }), 200
    
    @staticmethod
    def get_films():
        """Récupère une liste de films"""
        query = request.args.get('query', 'Action')
        page = request.args.get('page', 1)
        
        url = f"http://www.omdbapi.com/?s={query}&type=movie&page={page}&apikey={Config.OMDB_API_KEY}"
        response = requests.get(url).json()
        
        if response.get('Response') == 'True':
            films = response.get('Search', [])
            total_results = response.get('totalResults', 0)
            
            return jsonify({
                'films': films,
                'total': total_results,
                'page': page
            }), 200
        else:
            return jsonify({
                'error': response.get('Error', 'Impossible de récupérer les films'),
                'films': [],
                'total': 0
            }), 404
    
    @staticmethod
    def get_series():
        """Récupère une liste de séries"""
        query = request.args.get('query', 'Drama')
        page = request.args.get('page', 1)
        
        url = f"http://www.omdbapi.com/?s={query}&type=series&page={page}&apikey={Config.OMDB_API_KEY}"
        response = requests.get(url).json()
        
        if response.get('Response') == 'True':
            series = response.get('Search', [])
            total_results = response.get('totalResults', 0)
            
            return jsonify({
                'series': series,
                'total': total_results,
                'page': page
            }), 200
        else:
            return jsonify({
                'error': response.get('Error', 'Impossible de récupérer les séries'),
                'series': [],
                'total': 0
            }), 404
    
    @staticmethod
    def get_media_details(media_id):
        """Récupère les détails d'un film ou d'une série"""
        url = f"http://www.omdbapi.com/?i={media_id}&apikey={Config.OMDB_API_KEY}"
        response = requests.get(url).json()
        
        if response.get('Response') == 'True':
            media = Media(response)
            return jsonify(media.to_dict()), 200
        else:
            return jsonify({'error': 'Média non trouvé'}), 404
    
    @staticmethod
    def search_media():
        """Recherche de films et séries"""
        query = request.args.get('q', '')
        media_type = request.args.get('type', '')  # 'movie' ou 'series' ou vide pour tout
        
        if not query:
            return jsonify({'error': 'Paramètre de recherche manquant'}), 400
        
        url = f"http://www.omdbapi.com/?s={query}&apikey={Config.OMDB_API_KEY}"
        if media_type:
            url += f"&type={media_type}"
        
        response = requests.get(url).json()
        
        if response.get('Response') == 'True':
            results = response.get('Search', [])
            return jsonify({
                'results': results,
                'total': response.get('totalResults', 0)
            }), 200
        else:
            return jsonify({
                'results': [],
                'total': 0,
                'message': response.get('Error', 'Aucun résultat trouvé')
            }), 200
    
    @staticmethod
    def get_by_genre():
        """Récupère des médias par genre"""
        genre = request.args.get('genre', 'Action')
        media_type = request.args.get('type', 'movie')
        
        url = f"http://www.omdbapi.com/?s={genre}&type={media_type}&apikey={Config.OMDB_API_KEY}"
        response = requests.get(url).json()
        
        if response.get('Response') == 'True':
            results = response.get('Search', [])
            return jsonify({
                'results': results,
                'genre': genre,
                'type': media_type
            }), 200
        else:
            return jsonify({
                'results': [],
                'message': 'Aucun résultat trouvé'
            }), 200
