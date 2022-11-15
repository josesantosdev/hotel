from app import db, ma

from sqlalchemy import Column, BigInteger, DateTime, ForeignKey, Float

from marshmallow import fields

import datetime

from datetime import timedelta

from sqlalchemy.orm import relationship


class Hospedagem(db.Model):
    __tablename__ = 'Hospedagem'
    id_hospedagem = Column(BigInteger().with_variant(db.Integer, dialect_name="sqlite"), primary_key=True)
    checkin = Column(DateTime, nullable=False)
    checkout = Column(DateTime, nullable=False)
    id_quarto = Column(BigInteger, ForeignKey('Quarto.id_quarto'))
    id_hospede = Column(BigInteger, ForeignKey('Hospede.id_hospede'))
    dias = Column(BigInteger, nullable=False)
    
    
    #custo_total = Column(Float, nullable=False)
    #conta_cliente = Column(Float, nullable=False)
    #hospedagem_liquido = Column(Float, nullable=False)
    
    
    quarto = relationship('Quarto', back_populates="hospedagem")
    Hospede = relationship('Hospede', back_populates="hospedagem")

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
        include_fk = True
        include_relationships = True
        
        id_hospedagem = fields.Integer(dump_only=True)
        check_in = fields.DateTime()
        check_out = fields.DateTime()
        quarto_id = fields.Integer(required=True)
        hospede_id = fields.Integer(required=True)
        dias = fields.Integer
        
    _links = ma.Hyperlinks({
        "colletion": ma.URLFor("hospedagem_controller.consultar_hospedagem"),
        "self": ma.URLFor("hospedagem_controller.consultar_hospedagem_id", values=dict(id_hospedagem="<id_hospedagem>"))
    })
        
        
        
        
        
    
    