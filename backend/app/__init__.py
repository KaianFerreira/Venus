from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

from flask_cors import CORS

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type' 
    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    db.init_app(app)
    from .models import User, Post
    with app.app_context():
      db.create_all()


    from .auth import auth as auth_blueprint
 
    app.register_blueprint(auth_blueprint)

    from .landpage import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

