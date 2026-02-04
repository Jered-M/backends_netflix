class Media:
    """Modèle pour représenter un film ou une série"""
    
    def __init__(self, omdb_data):
        self.imdb_id = omdb_data.get('imdbID')
        self.title = omdb_data.get('Title')
        self.year = omdb_data.get('Year')
        self.type = omdb_data.get('Type')  # 'movie' ou 'series'
        self.poster = omdb_data.get('Poster')
        self.plot = omdb_data.get('Plot')
        self.genre = omdb_data.get('Genre')
        self.director = omdb_data.get('Director')
        self.actors = omdb_data.get('Actors')
        self.rating = omdb_data.get('imdbRating')
        self.runtime = omdb_data.get('Runtime')
    
    def to_dict(self):
        """Convertit l'objet en dictionnaire"""
        return {
            'imdbID': self.imdb_id,
            'title': self.title,
            'year': self.year,
            'type': self.type,
            'poster': self.poster,
            'plot': self.plot,
            'genre': self.genre,
            'director': self.director,
            'actors': self.actors,
            'rating': self.rating,
            'runtime': self.runtime
        }
    
    @staticmethod
    def from_omdb_list(omdb_list):
        """Convertit une liste de résultats OMDb en objets Media"""
        return [Media(item).to_dict() for item in omdb_list]
