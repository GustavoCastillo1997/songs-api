from db import db


song_music_style = db.Table(
    'song_music_style',
    db.Column('song_id', db.Integer, db.ForeignKey('song.id'), primary_key=True),
    db.Column('music_style_id', db.Integer, db.ForeignKey('music_style.id'), primary_key=True))

song_composer = db.Table(
    'song_composer',
    db.Column('song_id', db.Integer, db.ForeignKey('song.id'), primary_key=True),
    db.Column('composer_id', db.Integer, db.ForeignKey('composer.id'), primary_key=True))

song_service = db.Table(
    'song_service',
    db.Column('song_id', db.Integer, db.ForeignKey('song.id'), primary_key=True),
    db.Column('service_id', db.Integer, db.ForeignKey('service.id'), primary_key=True))

composer_music_style = db.Table(
    'composer_music_style',
    db.Column('composer_id', db.Integer, db.ForeignKey('composer.id'), primary_key=True),
    db.Column('music_style_id', db.Integer, db.ForeignKey('music_style.id'), primary_key=True))
