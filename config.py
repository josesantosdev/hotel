import os


class DevelopmentConfig():

    db_path = os.path.join(os.path.dirname(__file__), 'hotel.db')
    db_uri = 'sqlite:///{}'.format(db_path)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = 'filesystem'
    SQLALCHEMY_DATABASE_URI = db_uri
