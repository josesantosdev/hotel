from app import db, ma
from sqlalchemy import Column, BigInteger, String
from marshmallow import fields


class Hospede(db.Model):
    # atributos
    __tablename__ = 'Hospede'
    id_hospede = Column(BigInteger().with_variant(db.Integer, dialect_name="sqlite"), primary_key=True)
    nome = Column(String, nullable=False)
    cpf = Column(String)
    endereco = Column(String)
    email = Column(String, nullable=False)

    def __init__(self, nome, cpf, endereco, email):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.email = email

    def salvar(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self) -> str:
        return f'<id_hospede: {self.id_hospede}>'


class HospedeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Hospede
        load_instance = True
        sqla_session = db.session

        id_hospede = fields.Integer(dump_only=True)
        nome = fields.Str()
        cpf = fields.Str()
        endeceo = fields.Str()
        email = fields.Str()

    _links = ma.Hyperlinks({
        "colletion": ma.URLFor("hospede_controller.consultar_hospede"),
        "self": ma.URLFor("hospede_controller.consultar_hospede_id", values=dict(id_hospede="<id_hospede>"))
    })
