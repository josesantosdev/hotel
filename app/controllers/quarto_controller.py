from flask import Blueprint, request, json, Response

from app import db

from app.models.quarto_model import Quarto, QuartoSchema


class QuartoController(object):

    quarto_controller = Blueprint('quarto_controller', __name__)
    
    
    @quarto_controller.route('/quarto/cadastrar', methods=['POST'])
    def cadastrar_quarto():
        dados_request = request.get_json()
        quarto_schema = QuartoSchema()
        quarto = quarto_schema.load(dados_request)
        return custom_response(quarto_schema.dump(quarto.salvar()), 201)

    @quarto_controller.route('/quarto/consultar', methods=['GET'])
    def consultar_quarto():
        quarto = Quarto.query.all()
        quarto_schema = QuartoSchema()
        return (custom_response(quarto_schema.dump(quarto, many=True), 200))
    
    @quarto_controller.route('/quarto/consultar/<id_quarto>', methods=['GET'])
    def consultar_quarto_id(id_quarto):
        quarto = Quarto.query.filter_by(id_quarto=id_quarto).first()
        quarto_schema = QuartoSchema()
        return (custom_response(quarto_schema.dump(quarto), 200))
    
    @quarto_controller.route('/quarto/atualizar/<id_quarto>', methods=['PUT'])
    def atualizar_quarto(id_quarto):
        quarto_schema = QuartoSchema()
        query = Quarto.query.filter(Quarto.id_quarto == id_quarto)
        query.update(request.get_json())   
        return custom_response(quarto_schema.dump(query.first()), 201)

    @quarto_controller.route('/quarto/deletar/<id_quarto>', methods=['DELETE'])
    def deletar_quarto(id_quarto):
        quarto = Quarto.query.filter(Quarto.id_quarto == id_quarto)
        quarto.delete()
        db.session.commit()
        return custom_response({'Deletado':  f'id_quarto == {id_quarto}'}, 201)
        
    
def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
