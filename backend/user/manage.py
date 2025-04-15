from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from user.models import CodeHistory, db

manage_bp = Blueprint("manage", __name__)

@manage_bp.route("/history/<int:history_id>", methods=["DELETE"])
@jwt_required()
def delete_history(history_id):
    user_id = get_jwt_identity()
    history_item = CodeHistory.query.filter_by(id=history_id, user_id=user_id).first()

    if not history_item:
        return jsonify({"message": "History record not found or unauthorized"}), 404

    db.session.delete(history_item)
    db.session.commit()

    return jsonify({"message": "History record deleted successfully"}), 200
