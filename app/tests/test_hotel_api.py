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


'''
    Test Hospede
'''


def test_cadastrar_hospede(client):

    payload = json.dumps({
        "nome": "String",
        "cpf": "String",
        "endereco": "String",
        "email": "email@email11.com"
    })

    header = {"Content-Type": "application/json"}
    response = client.post(
        "http://127.0.0.1:5000/api/v1/hospede/cadastrar",
        data=payload,
        headers=header)

    assert response.status_code == 201


def test_consultar_todos_hospedes(client):
    response = client.get('http://127.0.0.1:5000/api/v1/hospede/consultar')
    data = json.loads(response.data.decode('utf-8'))
    assert type(data) == list
    assert response.status_code == 200


def test_consultar_hospedes_por_id(client):
    response = client.get('http://127.0.0.1:5000/api/v1/hospede/consultar/1')
    data = json.loads(response.data.decode('utf-8'))
    assert type(data) == dict
    assert response.status_code == 200


def test_alterar_hospede(client):

    payload = json.dumps({
        "nome": "String2",
        "cpf": "String2",
        "endereco": "String",
        "email": "email@email111.com"
    })

    header = {"Content-Type": "application/json"}
    response = client.put(
        "http://127.0.0.1:5000/api/v1/hospede/atualizar/1",
        data=payload,
        headers=header)

    assert response.status_code == 201


def test_deletar_hospede(client):
    response = client.delete('http://127.0.0.1:5000/api/v1/hospede/deletar/1')
    assert response.status_code == 201


'''
    Test Quarto
'''


def test_cadastrar_quarto(client):

    payload = json.dumps({
        "numero": 1,
        "tipo": "Suite",
        "preco": 500,
        "custo": 150
    })

    header = {"Content-Type": "application/json"}
    response = client.post(
        "http://127.0.0.1:5000/api/v1/quarto/cadastrar",
        data=payload,
        headers=header)

    assert response.status_code == 201


def test_consultar_todos_quartos(client):
    response = client.get('http://127.0.0.1:5000/api/v1/quarto/consultar')
    data = json.loads(response.data.decode('utf-8'))
    assert type(data) == list
    assert response.status_code == 200


def test_consultar_quarto_por_id(client):
    response = client.get('http://127.0.0.1:5000/api/v1/quarto/consultar/1')
    data = json.loads(response.data.decode('utf-8'))
    assert type(data) == dict
    assert response.status_code == 200


def test_alterar_quarto(client):

    payload = json.dumps({
        "numero": 101,
        "tipo": "Suite",
        "preco": 500,
        "custo": 150
    })

    header = {"Content-Type": "application/json"}
    response = client.put(
        "http://127.0.0.1:5000/api/v1/quarto/atualizar/1",
        data=payload,
        headers=header)

    assert response.status_code == 201


def test_deletar_hospede(client):
    response = client.delete('http://127.0.0.1:5000/api/v1/quarto/deletar/1')
    assert response.status_code == 201


'''
    Test hospedagem
'''


def test_cadastrar_hospedagem(client):
    payload = json.dumps({
        "quarto": 1,
        "hospede": "José",
        "dias": 7
    })

    header = {"Content-Type": "application/json"}

    response = client.post(
        "http://127.0.0.1:5000/api/v1/hospedagem/cadastrar",
        data=payload,
        headers=header)

    assert response.status_code == 201


def test_consultar_todos_hospedagens(client):
    response = client.get('http://127.0.0.1:5000/api/v1/hospede/consultar')
    data = json.loads(response.data.decode('utf-8'))
    assert type(data) == list
    assert response.status_code == 200


def test_consultar_hospedagem_por_id(client):
    response = client.get('http://127.0.0.1:5000/api/v1/hospede/consultar/1')
    data = json.loads(response.data.decode('utf-8'))
    assert type(data) == dict
    assert response.status_code == 200


def test_alterar_hospedagem(client):

    payload = json.dumps({
        "quarto": 1,
        "hospede": "José",
        "dias": 8
    })

    header = {"Content-Type": "application/json"}
    response = client.put(
        "http://127.0.0.1:5000/api/v1/hospedagem/atualizar/1",
        data=payload,
        headers=header)

    assert response.status_code == 201


def test_deletar_hospedagem(client):
    response = client.delete('http://127.0.0.1:5000/api/v1/hospedagem/deletar/1')
    assert response.status_code == 201


'''
    Test reserva hospedagem
'''


def test_cadastrar_reserva(client):

    payload = json.dumps({
        "quarto": 1,
        "hospede": "José",
        "dias": 7
    })

    header = {"Content-Type": "application/json"}
    response = client.post(
        "http://127.0.0.1:5000/api/v1/reserva/cadastrar",
        data=payload,
        headers=header)

    assert response.status_code == 201


def test_consultar_todos_reserva(client):
    response = client.get('http://127.0.0.1:5000/api/v1/reserva/consultar')
    data = json.loads(response.data.decode('utf-8'))
    assert type(data) == list
    assert response.status_code == 200


def test_consultar_reserva_por_id(client):
    response = client.get('http://127.0.0.1:5000/api/v1/reserva/consultar/1')
    data = json.loads(response.data.decode('utf-8'))
    assert type(data) == dict
    assert response.status_code == 200


def test_alterar_reserva(client):

    payload = json.dumps({
        "quarto": 2,
        "hospede": "José",
        "dias": 7
    })

    header = {"Content-Type": "application/json"}
    response = client.put(
        "http://127.0.0.1:5000/api/v1/reserva/atualizar/3",
        data=payload,
        headers=header)

    assert response.status_code == 201


def test_deletar_reserva(client):
    response = client.delete('http://127.0.0.1:5000/api/v1/reserva/deletar/3')
    assert response.status_code == 201
