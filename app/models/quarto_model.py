from app import db, ma

from sqlalchemy import Column, BigInteger, String, Float

from marshmallow import fields

from sqlalchemy.orm import relationship


class Quarto(db.Model):
    __tablename__ = 'Quarto'
    id_quarto = Column(BigInteger().with_variant(db.Integer, dialect_name="sqlite"), primary_key=True)
    numero = Column(BigInteger)
    tipo = Column(String)
    preco = Column(Float)
    custo = Column(Float)
    
    
    def __init__(self, numero, tipo, preco, custo):
        self.numero = numero
        self.tipo = tipo
        self.preco = preco
        self.custo = custo

    def salvar(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self) -> str:
        return f'<id_quarto: {self.id_quarto}>'


class QuartoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Quarto
        load_instance = True
        sqla_session = db.session

        id_quarto = fields.Integer(dump_only=True)
        numero = fields.Integer()
        tipo = fields.Str()
        preco = fields.Float()
        custo = fields.Float()

    _links = ma.Hyperlinks({
        "colletion": ma.URLFor("quarto_controller.consultar_quarto"),
        "self": ma.URLFor("quarto_controller.consultar_quarto_id", values=dict(id_quarto="<id_quarto>"))
    })
