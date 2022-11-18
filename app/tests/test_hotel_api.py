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


def test_cadastrar_hospede(client):
    
    payload = {
        "nome": "String",
        "cpf": "String",
        "endereco": "String",
        "email": "email@email11.com"
    }
    response = client.post(
                "http://127.0.0.1:5000/api/v1/hospede/cadastrar",
                data=json.dumps(payload),
                headers={"Content-Type": "application/json"}
            )
    assert response.status_code == 201
    

#test hospede Controllers
def test_consultar_todos_hospedes(client):
    response = client.get('http://127.0.0.1:5000/api/v1/hospede/consultar')
    data = json.loads(response.data.decode('utf-8'))
    assert type(data) == list
    assert response.status_code == 200
    

def test_consultar_hospedes_por_id(client):
    response = client.get('http://127.0.0.1:5000/api/v1/hospede/consultar/2')
    data = json.loads(response.data.decode('utf-8'))
    assert type(data) == dict
    assert response.status_code == 200
    

    
def test_alterar_hospede(client):
    pass
    
def test_deletar_hospede(client):
    request = client.delete('https://boiling-beach-14202.herokuapp.com/api/v1/hospede/deletar/1')
    data = json.loads(request)
    assert data['Deletado'] == 1
    
def test_consultar_quarto(client):
    pass

def test_consultar_quarto_por_id(client):
    pass

def test_cadastrar_quarto(client):
    payload ={
        "numero": 2,
        "tipo": "Suite",
        "preco": 500,
        "custo": 150
    }
    response = client.post(
                "http://127.0.0.1:5000/api/v1/quarto/cadastrar",
                data=json.dumps(payload),
                headers={"Content-Type": "application/json"}
            )
    assert response.status_code == 201

def test_alterar_quarto(client):
    pass

def test_deletar_quarto(client):
    pass

def test_consultar_hospedagem(client):
    pass

def test_consultar_hospedagem_por_id(client):
    pass

def test_cadastrar_hospedagem(client):
    payload = {
        "quarto": 1,
        "hospede": "José",
        "dias": 7
    }
    response = client.post(
                "http://127.0.0.1:5000/api/v1/hospedagem/cadastrar",
                data=json.dumps(payload),
                headers={"Content-Type": "application/json"}
            )
    assert response.status_code == 201

def test_alterar_hospedagem(client):
    pass

def test_deletar_hospedagem(client):
    pass

def test_consultar_reserva_hospedagem(client):
    pass

def test_consultar_reserva_hospedagem_por_id(client):
    pass

def test_cadastrar_reserva_hospedagem(client):
    pass

def test_alterar_reserva_hospedagem(client):
    pass

def test_deletar_reserva_hospedagem(client):
    pass
