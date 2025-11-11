from flask import Blueprint, jsonify

print("routes.py se está ejecutando correctamente")

routes = Blueprint("routes", __name__)

@routes.route("/test", methods=["GET"])
def test():
    return jsonify({"mensaje": "✅ Endpoint de prueba funcionando correctamente"})

from flask import request
from app.validator import clean_email, is_valid_email

@routes.route("/validate-emails", methods=["POST"])
def validate_emails():
    data = request.get_json()
    emails = data.get("emails", [])

    resultados = []
    for email in emails:
        limpio = clean_email(email)
        valido = is_valid_email(limpio)
        resultados.append({
            "original": email,
            "limpio": limpio,
            "valido": valido
        })

    return {"resultados": resultados}

@bp.route('/clean-emails', methods=['POST'])
def clean_emails():
    data = request.get_json()
    emails = data.get('emails', [])
    cleaned = [email for email in emails if is_valid_email(email)]
    return jsonify({"clean_emails": cleaned})