import pytest
from app.routes import routes
from app.validator import clean_email, is_valid_email
from flask import Flask

# 🔧 Configuración de app de prueba
@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(routes)
    app.testing = True
    return app.test_client()

# 🧪 Test: GET /test
def test_get_test(client):
    response = client.get("/test")
    assert response.status_code == 200
    assert response.get_json()["mensaje"].startswith("✅")

# 🧪 Test: POST /validate-emails
def test_post_validate_emails(client):
    payload = {
        "emails": [
            "ejemplo@dominio.com",
            "correo_invalido@",
            "otro@email.com"
        ]
    }
    response = client.post("/validate-emails", json=payload)
    assert response.status_code == 200
    data = response.get_json()["resultados"]
    assert len(data) == 3
    assert data[0]["valido"] is True
    assert data[1]["valido"] is False

# 🧪 Test: POST /clean-emails
def test_post_clean_emails(client):
    payload = {
        "emails": [
            "ejemplo@dominio.com",
            "correo_invalido@",
            "otro@email.com"
        ]
    }
    response = client.post("/clean-emails", json=payload)
    assert response.status_code == 200
    data = response.get_json()["clean_emails"]
    assert "ejemplo@dominio.com" in data
    assert "otro@email.com" in data
    assert "correo_invalido@" not in data

# 🧪 Test: POST /validate-emails sin campo "emails"
def test_validate_emails_missing_field(client):
    response = client.post("/validate-emails", json={})
    assert response.status_code == 400
    assert "error" in response.get_json()

# 🧪 Test: POST /validate-emails con campo incorrecto
def test_validate_emails_wrong_field(client):
    response = client.post("/validate-emails", json={"correo": ["a@b.com"]})
    assert response.status_code == 400
    assert "error" in response.get_json()

# 🧪 Test: POST /validate-emails con tipo incorrecto
def test_validate_emails_wrong_type(client):
    response = client.post("/validate-emails", json={"emails": "a@b.com"})
    assert response.status_code == 400
    assert "error" in response.get_json()

# 🧪 Test: POST /clean-emails sin campo "emails"
def test_clean_emails_missing_field(client):
    response = client.post("/clean-emails", json={})
    assert response.status_code == 400
    assert "error" in response.get_json()

# 🧪 Test: POST /clean-emails con tipo incorrecto
def test_clean_emails_wrong_type(client):
    response = client.post("/clean-emails", json={"emails": "a@b.com"})
    assert response.status_code == 400
    assert "error" in response.get_json()