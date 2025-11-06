from flask import Blueprint, request, jsonify
from app.validate_email import clean_email, is_valid_email

routes = Blueprint('routes', __name__)

# Ruta raíz para verificar que la API está activa
@routes.route('/')
def home():
    return "API funcionando correctamente en Render 🚀"

# Endpoint para limpiar y validar emails
@routes.route('/clean-emails', methods=['POST'])
def clean_emails():
    data = request.get_json()
    emails = data.get('emails', [])
    cleaned = []

    for email in emails:
        cleaned_email = clean_email(email)
        cleaned.append({
            "original": email,
            "cleaned": cleaned_email,
            "valid": is_valid_email(cleaned_email)  # ✅ Usamos el email limpio para validar
        })

    return jsonify({"results": cleaned})