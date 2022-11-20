from app import db, ma

from sqlalchemy import Column, BigInteger, String, Date

from app.models.quarto_model import Quarto

from marshmallow import fields

import datetime


class Reserva(db.Model):
    __tablename__ = 'Reserva'
    id_reserva = Column(BigInteger().with_variant(db.Integer, dialect_name="sqlite"), primary_key=True)
    checkin = Column(Date, nullable=False)
    quarto = Column(BigInteger)

    def __init__(self, checkin, quarto):
        self.checkin = checkin
        self.quarto = quarto
        
        if datetime.date.today() == checkin:
            quarto = Quarto.quarto_por_id(id_quarto=quarto)
            quarto.set_disponibilidade(False)
        
    def consultar_reserva(self, checkin):
        reserva = db.session.query(Reserva).filter(Reserva.checkin == checkin)
        return reserva.disponibilidade
    
    @staticmethod
    def reserva_por_checkin(id_reserva):
        return Reserva.query.filter(Reserva.id_reserva==id_reserva).first()

    def salvar(self):
        db.session.add(self)
        db.session.commit()
        return self


class ReservaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:

        model = Reserva
        load_instance = True
        sqla_session = db.session
        
        id_reserva = fields.Integer(dump_only=True)
        quarto = fields.Integer()
        disponibilidade = fields.Boolean(load_only=True)

    _links = ma.Hyperlinks({
        "colletion": ma.URLFor("reserva_controller.consultar_reserva"),
        "self": ma.URLFor("reserva_controller.consultar_reserva_id", values=dict(id_reserva="<id_reserva>"))
    })
