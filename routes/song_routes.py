from flask import Blueprint, request, jsonify
from models import Song
from db import db


songs_bp = Blueprint('songs', __name__)

@songs_bp.route('/songs', methods=['GET'])
def get_songs():
    songs = Song.query.all()
    return jsonify([song.to_dict() for song in songs]), 200

@songs_bp.route('/songs/<int:song_id>', methods=['GET'])
def get_song(song_id):
    song = Song.query.get_or_404(song_id)
    return jsonify(song.to_dict()), 200

@songs_bp.route('/songs', methods=['POST'])
def create_song():
    data = request.get_json()
    song = Song(**data)
    db.session.add(song)
    db.session.commit()
    return jsonify(song.to_dict()), 201

@songs_bp.route('/songs/<int:song_id>', methods=['PUT'])
def update_song(song_id):
    song = Song.query.get_or_404(song_id)
    data = request.get_json()
    for key, value in data.items():
        setattr(song, key, value)
    db.session.commit()
    return jsonify(song.to_dict()), 200

@songs_bp.route('/songs/<int:song_id>', methods=['DELETE'])
def delete_song(song_id):
    song = Song.query.get_or_404(song_id)
    db.session.delete(song)
    db.session.commit()
    return jsonify({'message': 'Deleted'}), 200
