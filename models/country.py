from db import db
from sqlalchemy import func


class Country(db.Model):
    __tablename__ = 'country'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    abreviation = db.Column(db.String(20), nullable=False)
    created_at = db.column(db.Datetime, nullable=False, default=func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=func.now(), onupdate=func.now())

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "abreviation": self.abreviation,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
