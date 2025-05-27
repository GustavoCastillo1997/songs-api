from flask import Blueprint, request, jsonify
from models import Composer
from db import db


composers_bp = Blueprint('composers', __name__)

@composers_bp.route('/composers', methods=['GET'])
def get_composers():
    composers = Composer.query.all()
    return jsonify([composer.to_dict() for composer in composers]), 200

@composers_bp.route('/composers/<int:composer_id>', methods=['GET'])
def get_composer(composer_id):
    composer = Composer.query.get_or_404(composer_id)
    return jsonify(composer.to_dict()), 200

@composers_bp.route('/composers', methods=['POST'])
def create_composer():
    data = request.get_json()
    composer = Composer(**data)
    db.session.add(composer)
    db.session.commit()
    return jsonify(composer.to_dict()), 201

@composers_bp.route('/composers/<int:composer_id>', methods=['PUT'])
def update_composer(composer_id):
    composer = Composer.query.get_or_404(composer_id)
    data = request.get_json()
    for key, value in data.items():
        setattr(composer, key, value)
    db.session.commit()
    return jsonify(composer.to_dict()), 200

@composers_bp.route('/composers/<int:composer_id>', methods=['DELETE'])
def delete_composer(composer_id):
    composer = Composer.query.get_or_404(composer_id)
    db.session.delete(composer)
    db.session.commit()
    return jsonify({'message': 'Deleted'}), 200
