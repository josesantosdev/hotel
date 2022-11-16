import pytest
from app import create_app
import json


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app
    
@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

#test hospede Controllers
def test_consultar_todos_hospedes(client):
    response = client.get('http://127.0.0.1:5000/api/v1/hospede/consultar')
    data = json.loads(response.data.decode('utf-8'))
    assert type(data) == list
    assert data[0]["id_hospede"] == 3
    assert data[1]["id_hospede"] == 4
    assert response.status_code == 200
    

def test_consultar_hospedes_por_id(client):
    response = client.get('http://127.0.0.1:5000/api/v1/hospede/consultar/3')
    data = json.loads(response.data.decode('utf-8'))
    assert type(data) == dict
    assert data["id_hospede"] == 3
    assert response.status_code == 200
    
def test_cadastrar_hospede(client):
    pass
    
def test_alterar_hospede(client):
    pass
    
def test_deletar_hospede(client):
    pass
    
    
    