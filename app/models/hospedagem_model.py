from app import db, ma

from sqlalchemy import Column, BigInteger, DateTime, String, Float

from marshmallow import fields

import datetime

from datetime import timedelta


class Hospedagem(db.Model):
    __tablename__ = 'Hospedagem'
    id_hospedagem = Column(BigInteger().with_variant(db.Integer, dialect_name="sqlite"), primary_key=True)
    checkin = Column(DateTime, nullable=False)
    checkout = Column(DateTime, nullable=False)
    id_quarto = Column(String)
    id_hospede = Column(String)
    dias = Column(BigInteger, nullable=False)
    custo_total = Column(Float, nullable=False)
    conta_cliente = Column(Float, nullable=False)
    hospedagem_liquido = Column(Float, nullable=False)
    

    def __init__(self, id_quarto, id_hospede, dias):
        self.checkin = datetime.date.today()
        self.checkout = self.checkin + timedelta(days=self.dias)
        self.id_quarto = id_quarto
        self.id_hospede = id_hospede
        self.dias = dias
        
    def salvar(self):
        db.session.add(self)
        db.session.commit()
        return self
        
    def __repr__(self) -> str:
        return f'<id_hospedagem: {self.id_hospedagem}>'


class HospedagemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Hospedagem
        load_instance = True
        session = db.session
        
        id_hospedagem = fields.Integer(dump_only=True)
        check_in = fields.DateTime()
        check_out = fields.DateTime()
        quarto_id = fields.Integer()
        hospede_id = fields.Integer()
        dias = fields.Integer
        
    _links = ma.Hyperlinks({
        "colletion": ma.URLFor("hospedagem_controller.consultar_hospedagem"),
        "self": ma.URLFor("hospedagem_controller.consultar_hospedagem_id", values=dict(id_hospedagem="<id_hospedagem>"))
    })
        
        
        
        
        
    
    