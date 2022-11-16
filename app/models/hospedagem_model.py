from app import db, ma

from sqlalchemy import Column, BigInteger, String, Float, Date

from marshmallow import fields

import datetime

from datetime import timedelta

from app.models.quarto_model import Quarto



class Hospedagem(db.Model):
    __tablename__ = 'Hospedagem'
    id_hospedagem = Column(BigInteger().with_variant(db.Integer, dialect_name="sqlite"), primary_key=True)
    checkin = Column(Date, nullable=False)
    checkout = Column(Date, nullable=False)
    quarto = Column(BigInteger)
    hospede = Column(String)
    dias = Column(BigInteger, nullable=False)
    custo_total = Column(BigInteger)
    conta_cliente = Column(BigInteger)
    hospedagem_liquido = Column(BigInteger)
    

    def __init__(self, quarto, hospede, dias):
        self.checkin = datetime.date.today()
        self.dias = dias
        self.checkout = self.checkin + timedelta(days=self.dias)
        self.quarto = quarto
        self.hospede = hospede
        
        quarto_id = Quarto.quarto_por_id(id_quarto=self.quarto)
        
        self.custo_total = quarto_id.custo * self.dias
        self.conta_cliente = quarto_id.preco * self.dias
        self.hospedagem_liquido = self.conta_cliente - self.custo_total
        
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
        quarto = fields.Integer()
        hospede = fields.String()
        dias = fields.Integer()
        custo_total = fields.Integer(domp_only=True)
        conta_cliente = fields.Integer(domp_only=True)
        hospedagem_liquido = fields.Integer(domp_only=True)
        
    _links = ma.Hyperlinks({
        "colletion": ma.URLFor("hospedagem_controller.consultar_hospedagem"),
        "self": ma.URLFor("hospedagem_controller.consultar_hospedagem_id", values=dict(id_hospedagem="<id_hospedagem>"))
    })
        
        
        
        
        
    
    