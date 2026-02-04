from flask import Blueprint
from controllers.media_controller import MediaController

media_bp = Blueprint('media', __name__, url_prefix='/api')

# Routes pour les médias
media_bp.route('/trending', methods=['GET'])(MediaController.get_trending)
media_bp.route('/films', methods=['GET'])(MediaController.get_films)
media_bp.route('/series', methods=['GET'])(MediaController.get_series)
media_bp.route('/media/<string:media_id>', methods=['GET'])(MediaController.get_media_details)
media_bp.route('/search', methods=['GET'])(MediaController.search_media)
media_bp.route('/genre', methods=['GET'])(MediaController.get_by_genre)
