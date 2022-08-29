from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'e7bf9f9ed2bebe4b2f9d01ed20c33d443a20b5be36509a7bd43259011fa77346dea1fbdbb6ee323a49bb18c2e2cb6481d19ba5e261ea483df842dddd9901bb09'
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app