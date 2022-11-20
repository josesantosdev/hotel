from flask import Blueprint, request, json, Response

from app.models.reserva_hospedagem_model import Reserva, ReservaSchema

from app import db


class ReservaController(object):

    reserva_controller = Blueprint('reserva_controller', __name__)

    @reserva_controller.route('/reverva/cadastrar', methods=['POST'])
    def cadastrar_reserva():
        request_data = request.get_json()
        reserva_schema = ReservaSchema()
        reserva = reserva_schema.load(request_data)
        return custom_response(reserva_schema.dump(reserva.salvar()), 201)

    @reserva_controller.route('/reserva/consultar', methods=['GET'])
    def consultar_reserva():
        reserva = Reserva.query.all()
        reserva_schema = ReservaSchema(many=True)
        return custom_response(reserva_schema.dump(reserva), 200)

    @reserva_controller.route('/reverva/consultar/<id_reserva>', methods=['GET'])
    def consultar_reserva_id(id_reserva):
        reserva = Reserva.query.filter_by(id_reserva=id_reserva)
        reserva_schema = ReservaSchema()
        return custom_response(reserva_schema.dump(reserva), 200)

    @reserva_controller.route('/reverva/atualizar/<id_reserva>', methods=['PUT'])
    def alterar_reserva(id_reserva):
        reserva_schema = ReservaSchema()
        query = Reserva.query.filter(Reserva.id_reserva == id_reserva)
        query.update(request.get_json())
        return custom_response(reserva_schema.dump(query.first()), 201)

    @reserva_controller.route('/reverva/deletar/<id_reserva>', methods=['DELETE'])
    def deletar_reserva(id_reserva):
        reserva = Reserva.query.filter(Reserva.id_reserva == id_reserva)
        reserva.delete()
        db.session.commit()
        return custom_response({'Deletado':  f'id_reserva == {id_reserva}'}, 201)


def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
