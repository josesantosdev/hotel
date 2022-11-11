# Hotel API
- Projeto proposto na UC Gestão de Qualidade de Software.
- API RESTfull para gestão das hospedagens de um hotel.

### Dependencies
- Flask
- SQLAlchemy
- Flask Migrate
- SQLite
- Marshmallow
- Pytest

### Clone this repo

```sh
git clone git@github.com:josesantosdev/hotel.git #ssh
git clone https://github.com/josesantosdev/hotel.git #https
```

### How to run this project
```sh
pip install pipenv
pipenv install -r requirements.txt
export FLASK_APP=app
export FLASK_DEBUG=1
flask run
```

### Run unit tests
```sh
pytest
```

### Make migrations if db is setup
```sh
flask db init
flask db migrate
flask db upgrade
```