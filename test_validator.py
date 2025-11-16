import pytest
from app.validator import clean_email, is_valid_email, extract_domain

def test_clean_email_basic():
    assert clean_email("  Ejemplo@Dominio.COM  ") == "ejemplo@dominio.com"

def test_clean_email_invisible():
    assert clean_email("correo\u200b@dominio.com") == "correo@dominio.com"

def test_clean_email_spaces_inside():
    assert clean_email("correo @dominio.com") == "correo@dominio.com"

def test_valid_email_true():
    assert is_valid_email("usuario@gmail.com") is True

def test_valid_email_false():
    assert is_valid_email("correo_invalido@") is False

def test_extract_domain_valid():
    assert extract_domain("usuario@gmail.com") == "gmail.com"

def test_extract_domain_invalid():
    assert extract_domain("correo_invalido@") is None