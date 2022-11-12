from app import db, ma
from sqlalchemy import Column, BigInteger, String, Float, Boolean
from marshmallow import fields


class Quarto(db.model):
    id_quarto = Column(BigInteger().with_variant(db.Integer, dialect_name="sqlite"), primary_key=True)
    numero = Column(BigInteger)
    tipo = Column(String)
    preco = Column(Float)
    custo = Column(Float)
    
    
    
    def __init__(self, numero, tipo, preco, custo, disponibilidade):
        self.numero = numero
        self.tipo = tipo
        self.preco = preco
        self.custo = custo
        
      
    def salvar(self):
        db.session.add(self)
        db.session.commit()
    
    def __repr__(self) -> str:
        return f'<id_quarto: {self.id_quarto}>'
    

  
class QuartoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Quarto
        load_instance = True
        sqla_session = db.session
        
        id_quarto = fields.Int()
        numero = fields.Int()
        tipo = fields.Str()
        preco = fields.Float()
        custo = fields.Float()

        
    '''
     _links = ma.Hyperlinks({
        "colletion": ma.URLFor("hospede_controller.consultar_hospede"),
        "self": ma.URLFor("hospede_controller.consultar_hospede_id", values=dict(id_hospede="<id_hospede>"))
    })
  
    '''


