from db import db
from sqlalchemy import func
from models.association import song_service, song_composer, song_music_style


class Song(db.Model):
    __tablename__ = 'song'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Time, nullable=False, default='00:00:00')
    release_date = db.Column(db.DateTime, nullable=False)
    instrumental = db.Column(db.Boolean, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=func.now(), onupdate=func.now())

    music_styles = db.relationship('MusicStyle', secondary=song_music_style, backref='songs')
    composers = db.relationship('Composer', secondary=song_composer, backref='songs')
    services = db.relationship('Service', secondary=song_service, backref='songs')

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "duration": self.duration,
            "release_date": self.release_date,
            "instrumental": self.instrumental,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
