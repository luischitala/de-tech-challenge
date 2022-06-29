from fastapi.testclient import TestClient
from internal.app import backend_app 

app = backend_app()
client = TestClient(app)

def test_mayoralties():
    response = client.get('/api/v1/alcaldias/')
    assert response.status_code == 200


