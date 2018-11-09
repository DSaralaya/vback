from app.config import Config
from flask import Flask

def create_app(config_class=Config):
      app = Flask(__name__)
      app.config.from_object(Config)

      from app.main.controller.user_controller import user
      app.register_blueprint(user)

      return app

