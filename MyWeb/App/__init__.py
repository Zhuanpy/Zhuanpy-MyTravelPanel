from flask import Flask
from .views import dex
from .routes_visa import visa_blue
from .route_flight import flight_blue
from .routes_files import files_blue
from .routes_statement import statement_blue


def create_app():
    app = Flask(__name__)
    app.register_blueprint(dex)
    app.register_blueprint(visa_blue)
    app.register_blueprint(flight_blue)
    app.register_blueprint(files_blue)
    app.register_blueprint(statement_blue)
    return app
