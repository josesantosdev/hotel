from flask import Blueprint, json, Response, request

from app import db

from app.models.hospede_model import Hospede, HospedeSchema


class HospedeController(object):

    hospede_controller = Blueprint('hospede_controller', __name__)


    @hospede_controller.route('/hospede/cadastrar', methods=['POST'])
    def cadastrar_hospede():
        dados_requisicao = request.get_json()
        hospede_schema = HospedeSchema()
        hospede = hospede_schema.load(dados_requisicao)
        return custom_response(hospede_schema.dump(hospede.salvar()), 201)
    
    @hospede_controller.route('/hospede/consultar', methods=['GET'])
    def consultar_hospede():
        hospede = Hospede.query.all()
        hospede_schema = HospedeSchema(many=True)
        return custom_response(hospede_schema.dump(hospede), 200)
    
    @hospede_controller.route('/hospede/consultar/<id_hospede>', methods=['GET'])
    def consultar_hospede_id(id_hospede):
        hospede = Hospede.query.filter_by(id_hospede=id_hospede).first()
        hospede_schema = HospedeSchema()
        return custom_response(hospede_schema.dump(hospede),200)

    @hospede_controller.route('/hospede/atualizar/<id_hospede>', methods=['PUT'])
    def alterar_hospede(id_hospede):
        hospede_schema = HospedeSchema()
        query = Hospede.query.filter(Hospede.id_hospede == id_hospede)
        query.update(request.get_json())
        return custom_response(hospede_schema.dump(query.first()), 201)

    @hospede_controller.route('/hospede/deletar/<id_hospede>', methods=['DELETE'])
    def deletar_hospede(id_hospede):
        hospede = Hospede.query.filter(Hospede.id_hospede == id_hospede)
        hospede.delete()
        db.session.commit()
        return custom_response({'Deletado':  f'id_hospede: {id_hospede}'}, 201)
        


def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
