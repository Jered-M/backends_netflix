from flask import Blueprint
from controllers.user_controller import UserController

user_bp = Blueprint('user', __name__, url_prefix='/api/user')

# Routes utilisateur
user_bp.route('/<int:user_id>/favorites', methods=['GET'])(UserController.get_favorites)
user_bp.route('/<int:user_id>/favorites', methods=['POST'])(UserController.add_to_favorites)
user_bp.route('/<int:user_id>/favorites', methods=['DELETE'])(UserController.remove_from_favorites)
user_bp.route('/<int:user_id>/history', methods=['GET'])(UserController.get_history)
user_bp.route('/<int:user_id>/history', methods=['POST'])(UserController.add_to_history)
