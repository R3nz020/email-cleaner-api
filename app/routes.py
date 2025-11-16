from flask import Blueprint, request, jsonify
from app.validator import clean_and_validate_emails, extract_domain

routes = Blueprint('routes', __name__)

@routes.route("/validate-emails", methods=["POST"])
def validate_emails():
    data = request.get_json()
    emails = data.get("emails", [])

    cleaned, invalid = clean_and_validate_emails(emails)

    resultados = []
    for email in emails:
        limpio = email.strip().lower().replace('\u200b', '').replace(' ', '')
        valido = email in cleaned
        resultados.append({
            "original": email,
            "limpio": limpio,
            "valido": valido
        })

    return jsonify({"resultados": resultados})

@routes.route('/clean-emails', methods=['POST'])
def clean_emails_endpoint():
    try:
        data = request.get_json(force=True)
        emails = data.get('emails', [])
        print(f"📩 Datos recibidos: {data}")
        cleaned, invalid = clean_and_validate_emails(emails)
        print(f"✅ Limpios: {cleaned} | ❌ Inválidos: {invalid}")
        return jsonify({
            'cleaned_emails': cleaned,
            'invalid_emails': invalid
        })
    except Exception as e:
        print(f"⚠️ Error en /clean-emails: {e}")
        return jsonify({"error": str(e)}), 400