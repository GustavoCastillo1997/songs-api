from flask import Blueprint, request, jsonify
from models import Country
from db import db


countries_bp = Blueprint('countries', __name__)

@countries_bp.route('/countries', methods=['GET'])
def get_countries():
    countries = Country.query.all()
    return jsonify([country.to_dict() for country in countries]), 200

@countries_bp.route('/countries/<int:country_id>', methods=['GET'])
def get_country(country_id):
    country = Country.query.get_or_404(country_id)
    return jsonify(country.to_dict()), 200

@countries_bp.route('/countries', methods=['POST'])
def create_country():
    data = request.get_json()
    country = Country(**data)
    db.session.add(country)
    db.session.commit()
    return jsonify(country.to_dict()), 201

@countries_bp.route('/countries/<int:country_id>', methods=['PUT'])
def update_country(country_id):
    country = Country.query.get_or_404(country_id)
    data = request.get_json()
    for key, value in data.items():
        setattr(country, key, value)
    db.session.commit()
    return jsonify(country.to_dict()), 200

@countries_bp.route('/countries/<int:country_id>', methods=['DELETE'])
def delete_country(country_id):
    country = Country.query.get_or_404(country_id)
    db.session.delete(country)
    db.session.commit()
    return jsonify({'message': 'Deleted'}), 200
