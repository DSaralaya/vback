from app.config import Config
from flask import Flask

def create_app(config_class=Config):
      app = Flask(__name__)
      app.config.from_object(Config)

      from app.main.controller.user_controller import user
      from app.main.util.auth import auth

      app.register_blueprint(user)
      app.register_blueprint(auth)
      return app

