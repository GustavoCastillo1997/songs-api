from flask import Blueprint, request, jsonify
from models import MusicStyle
from db import db


music_styles_bp = Blueprint('music_styles', __name__)

@music_styles_bp.route('/music_styles', methods=['GET'])
def get_music_styles():
    music_styles = MusicStyle.query.all()
    return jsonify([music_style.to_dict() for music_style in music_styles]), 200

@music_styles_bp.route('/music_styles/<int:music_style_id>', methods=['GET'])
def get_music_style(music_style_id):
    music_style = MusicStyle.query.get_or_404(music_style_id)
    return jsonify(music_style.to_dict()), 200

@music_styles_bp.route('/music_styles', methods=['POST'])
def create_music_style():
    data = request.get_json()
    music_style = MusicStyle(**data)
    db.session.add(music_style)
    db.session.commit()
    return jsonify(music_style.to_dict()), 201

@music_styles_bp.route('/music_styles/<int:music_style_id>', methods=['PUT'])
def update_music_style(music_style_id):
    music_style = MusicStyle.query.get_or_404(music_style_id)
    data = request.get_json()
    for key, value in data.items():
        setattr(music_style, key, value)
    db.session.commit()
    return jsonify(music_style.to_dict()), 200

@music_styles_bp.route('/music_styles/<int:music_style_id>', methods=['DELETE'])
def delete_music_style(music_style_id):
    music_style = MusicStyle.query.get_or_404(music_style_id)
    db.session.delete(music_style)
    db.session.commit()
    return jsonify({'message': 'Deleted'}), 200
