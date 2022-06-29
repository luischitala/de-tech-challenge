from fastapi.testclient import TestClient
from internal.app import backend_app 

app = backend_app()
client = TestClient(app)

def test_transport_units():
    response = client.get('/api/v1/metrobuses/')
    assert response.status_code == 200

def test_transport_unit_by_id():
    res = client.get("/api/v1/metrobuses/1")
    assert res.status_code == 200

def test_transport_unit_by_mayoralty():
    res = client.get("/api/v1/metrobuses/alcaldia/Tlalpan")
    assert res.status_code == 200