from flask import Blueprint, request, jsonify
from models import Service
from db import db


services_bp = Blueprint('services', __name__)

@services_bp.route('/services', methods=['GET'])
def get_services():
    services = Service.query.all()
    return jsonify([service.to_dict() for service in services]), 200

@services_bp.route('/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    service = Service.query.get_or_404(service_id)
    return jsonify(service.to_dict()), 200

@services_bp.route('/services', methods=['POST'])
def create_service():
    data = request.get_json()
    service = Service(**data)
    db.session.add(service)
    db.session.commit()
    return jsonify(service.to_dict()), 201

@services_bp.route('/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    service = Service.query.get_or_404(service_id)
    data = request.get_json()
    for key, value in data.items():
        setattr(service, key, value)
    db.session.commit()
    return jsonify(service.to_dict()), 200

@services_bp.route('/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    service = Service.query.get_or_404(service_id)
    db.session.delete(service)
    db.session.commit()
    return jsonify({'message': 'Deleted'}), 200
