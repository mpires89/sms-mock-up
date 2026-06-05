import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_enviar_sms_provedor_primario():
    response = client.post(
        "/enviar-sms",
        json={"telefone": "11999999999", "mensagem": "Teste API primário", "provedor": "primary"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "sucesso"
    assert "Provedor Primário" in data["detalhe"]
    assert "11999999999" in data["detalhe"]

def test_enviar_sms_provedor_secundario():
    response = client.post(
        "/enviar-sms",
        json={"telefone": "11888888888", "mensagem": "Teste API secundário", "provedor": "secondary"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "sucesso"
    assert "Provedor Secundário" in data["detalhe"]
    assert "11888888888" in data["detalhe"]

def test_enviar_sms_provedor_invalido():
    response = client.post(
        "/enviar-sms",
        json={"telefone": "11888888888", "mensagem": "Teste API invalido", "provedor": "invalido"}
    )
    assert response.status_code == 400
    data = response.json()
    assert "Provedor indefinido ou inválido" in data["detail"]

def test_enviar_sms_sem_provedor_usa_default():
    response = client.post(
        "/enviar-sms",
        json={"telefone": "11999999999", "mensagem": "Teste default"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "sucesso"
    assert "Provedor Primário" in data["detalhe"]
