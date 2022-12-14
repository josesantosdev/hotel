from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_marshmallow import Marshmallow

from flask_migrate import Migrate


db = SQLAlchemy()
ma = Marshmallow()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')
    db.init_app(app)
    ma.init_app(app)
    Migrate(app, db)

    # Models
    
    from app.models.hospede_model import Hospede
    
    from app.models.quarto_model import Quarto
    
    from app.models.hospedagem_model import Hospedagem
    
    from app.models.reserva_hospedagem_model import Reserva
   
    #controllers
    
    from app.controllers.hospede_contoller import HospedeController
    
    from app.controllers.doc_controller import DocumentationControoler
    
    from app.controllers.quarto_controller import QuartoController
    
    from app.controllers.hospedagem_controller import HospedagemController
    
    from app.controllers.reserva_hospedagem_controller import ReservaController

     # Registro das blueprints
     
    app.register_blueprint(HospedeController.hospede_controller, url_prefix='/api/v1')
    
    app.register_blueprint(DocumentationControoler.documentation_controller, url_prefix='/api/v1')
    
    app.register_blueprint(QuartoController.quarto_controller, url_prefix='/api/v1')
    
    app.register_blueprint(HospedagemController.hospedagem_controller, url_prefix='/api/v1')
    
    app.register_blueprint(ReservaController.reserva_controller, url_prefix='/api/v1')
    


    return app
