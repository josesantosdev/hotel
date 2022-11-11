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

### Cloning this repo

```sh
    git clone url_repo
```

### How to run this project
```sh
pip install pipenv
pipenv install -r requirements.txt
export FLASK_APP=app
export FLASK_DEBUG=1
flask run
```

### To run tests
```sh
pytest
```

### Migrations if db is not available
```sh
flask db init
flask db migrate
flask db upgrade
```