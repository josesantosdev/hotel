from flask import Blueprint, request, json, Response

from app.models.hospedagem_model import Hospedagem, HospedagemSchema

from app import db


class HospedagemController(object):

    hospedagem_controller = Blueprint('hospedagem_controller', __name__)

    @hospedagem_controller.route('/hospedagem/cadastrar', methods=['POST'])
    def cadastrar_hospedagem():
        request_data = request.get_json()
        hospedagem_schema = HospedagemSchema(partial=True)
        hospedagem = hospedagem_schema.load(request_data)
        return custom_response(hospedagem_schema.dump(hospedagem.salvar()), 201)

    @hospedagem_controller.route('/hospedagem/consultar', methods=['GET'])
    def consultar_hospedagem():
        hospedagem = Hospedagem.query.all()
        hospedagem_schema = HospedagemSchema(many=True)
        return custom_response(hospedagem_schema.dump(hospedagem), 200)

    @hospedagem_controller.route('/hospedagem/consultar/<id_hospedagem>', methods=['GET'])
    def consultar_hospedagem_id(id_hospedagem):
        hospedagem_por_id = Hospedagem.query.filter_by(id_hospedagem=id_hospedagem).first()
        hospedagem_schema = HospedagemSchema()
        return custom_response(hospedagem_schema.dump(hospedagem_por_id), 200)

    @hospedagem_controller.route('/hospedagem/atualizar/<id_hospedagem>', methods=['PUT'])
    def atualiazar_hospedagem(id_hospedagem):
        hospede_schema = HospedagemSchema(partial=False)
        query = Hospedagem.query.filter(Hospedagem.id_hospedagem == id_hospedagem)
        query.update(request.get_json())
        return custom_response(hospede_schema.dump(query.fisrt()), 201)

    @hospedagem_controller.route('/hospedagem/deletar/<id_hospedagem>', methods=['DELETE'])
    def deletar_hospedagem(id_hospedagem):
        hospedagem = Hospedagem.query.filter(Hospedagem.id_hospedagem == id_hospedagem)
        hospedagem.delete()
        db.session.commit()
        return custom_response({'Deletado':  f'id_hospedagem == {id_hospedagem}'}, 201)


def custom_response(res, status_code):
    return Response(
        mimetype='application/json',
        response=json.dumps(res),
        status=status_code)
