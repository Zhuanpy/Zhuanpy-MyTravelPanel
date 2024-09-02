from flask import Flask
from .views import dex

from .code.routes_visa import bp as visa_routes
from .code.route_flight import fb as flight_routes
from .code.routes_files import fpb as files_routes
from .code.routes_statement import sb as statement_routes


def create_app():
    app = Flask(__name__)
    app.register_blueprint(dex)
    app.register_blueprint(visa_routes)
    app.register_blueprint(flight_routes)
    app.register_blueprint(files_routes)
    app.register_blueprint(statement_routes)

    return app
