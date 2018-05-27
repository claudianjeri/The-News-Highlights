from flask import Flask  # importing Flask class fro flask module
from .config import config_options  # getting config.py
# import the bootstrap class from flask_bootstrap
from flask_bootstrap import Bootstrap


def create_app(config_name):

    app = Flask(__name__)
# Initializing the app


# connects to the config.py file
app.config.from_object(config_options[config_name])
    bootstrap.init_app(app)  # initializing boostrap flask extension
    # Registering the blueprint
        from .main import main as main_blueprint
        app.register_blueprint(main_blueprint)
# setting config
    from .requests import configure_request
    configure_request(app)
return app  # this will help in the creation of views
