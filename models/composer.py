from db import db
from sqlalchemy import func
from models.association import composer_music_style


class Composer(db.Model):
    __tablename__ = 'composer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date, nullable=True)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=func.now(), onupdate=func.now())

    country = db.relationship('Country', backref='composers')
    music_styles = db.relationship('MusicStyle', secondary=composer_music_style, backref='composers')
