from app import db, ma

from sqlalchemy import Column, BigInteger, String, Date

from marshmallow import fields

import datetime

from app.models.quarto_model import Quarto





class Reserva(db.Model):
    __tablename__ = 'Reserva'
    id_reserva = Column(BigInteger().with_variant(db.Integer, dialect_name="sqlite"), primary_key=True)
    checkin = Column(Date, nullable=False)
    quarto = Column(BigInteger)
    hospede_cpf = Column(String)

    def __init__(self,id_reserva, checkin, quarto, hospede_cpf):
        self.id_reserva = id_reserva
        self.checkin = checkin
        self.quarto = Quarto.quarto_por_id(quarto)
        self.hospede_cpf = hospede_cpf

    def salvar(self):
        db.session.add(self)
        db.session.commit()
        return self

class ReservaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:

        model = Reserva
        load_instance = True
        sqla_session = db.session

    '''_links = ma.Hyperlinks({
        "colletion": ma.URLFor("reserva_controller.consultar_reserva"),
        "self": ma.URLFor("reserva_controller.consultar_reserva_id", values=dict(id_reserva="<id_reserva>"))
    })'''

       





        
 