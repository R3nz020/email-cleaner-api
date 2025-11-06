from flask import Blueprint, request, jsonify
from app.validator import clean_email, is_valid_email

routes = Blueprint('routes', __name__)

@routes.route('/clean-emails', methods=['POST'])
def clean_emails():
    data = request.get_json()
    emails = data.get('emails', [])
    cleaned = []

    for email in emails:
        e = clean_email(email)
        cleaned.append({
            "original": email,
            "cleaned": e,
            "valid": is_valid_email(e)
        })

    return jsonify({"results": cleaned})