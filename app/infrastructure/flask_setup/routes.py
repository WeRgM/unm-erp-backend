from flask import request, jsonify
from flask import Blueprint
from app.infrastructure.repository.sql_alchemy_user_repository import SQLAlchemyUserRepository
from app.domain.entities.user import User

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['GET'])
def get_all_users():
    user_repository = SQLAlchemyUserRepository()
    users = user_repository.get_all()
    return jsonify([user.serialize() for user in users]), 200

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user_repository = SQLAlchemyUserRepository()
    user = user_repository.get_by_id(user_id)
    if user is None:
        return jsonify({'message': 'User does not exist'}), 404
    return jsonify(user.serialize()), 200

@user_bp.route('/users', methods=['POST'])
def create_user():
    user_data = request.json
    user_repository = SQLAlchemyUserRepository()
    user = User(**user_data)
    user_repository.create(user)
    return jsonify({'message': 'User created'}), 201

@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user_repository = SQLAlchemyUserRepository()
    user = user_repository.get_by_id(user_id)

    if user is None:
        return jsonify({'message': 'User does not exist'}), 404
    update_data = request.json
    for key, value in update_data.items():
        setattr(user, key, value)
    user_repository.update(user)
    return jsonify({'message': 'User updated'}), 200

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user_repository = SQLAlchemyUserRepository()
    user = user_repository.get_by_id(user_id)
    if user is None:
        return jsonify({'message': 'User does not exist'}), 404
    user_repository.delete(user)

def init_app(app):
    app.register_blueprint(user_bp, url_prefix='/api')