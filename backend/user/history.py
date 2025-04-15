from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from user.models import db, CodeHistory

history_bp = Blueprint("history", __name__)

@history_bp.route("/history", methods=["GET"])
@jwt_required()
def get_history():
    user_id = get_jwt_identity()
    history = CodeHistory.query.filter_by(user_id=user_id).all()
    return jsonify([
        {
            "id": record.id,
            "original_code": record.original_code,
            "optimized_code": record.optimized_code
        }
        for record in history
    ]), 200

@history_bp.route("/history/<int:history_id>", methods=["DELETE"])
@jwt_required()
def delete_history(history_id):
    user_id = get_jwt_identity()
    record = CodeHistory.query.filter_by(id=history_id, user_id=user_id).first()
    if not record:
        return jsonify({"message": "Record not found"}), 404
    db.session.delete(record)
    db.session.commit()
    return jsonify({"message": "Record deleted successfully"}), 200
