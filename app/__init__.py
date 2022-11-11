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
   
    # Registro das blueprints
    
    from app.controllers.hospede_contoller import HospedeController

    app.register_blueprint(HospedeController.hospede_controller, url_prefix='/api/v1')

    return app
