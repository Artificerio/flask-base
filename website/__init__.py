from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    #configure flask
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:0305@localhost:5432/test'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = 'webiste/images/'

    #database
    db.init_app(app)
    from .models import Img
    create_database(app)

    #blueprints
    from .click import click
    from .index import index
    app.register_blueprint(click)
    app.register_blueprint(index)

    return app


def create_database(app):
    with app.app_context():
        db.create_all(app=app)