from flask import Flask
from .views import dex

from .routes_visa import visa_blue
from .route_flight import flight_blue
from .routes_files import files_blue
from .routes_statement import statement_blue
from .exts import init_exts
import pymysql

pymysql.install_as_MySQLdb()


def create_app():
    app = Flask(__name__)
    app.register_blueprint(dex)
    app.register_blueprint(visa_blue)
    app.register_blueprint(flight_blue)
    app.register_blueprint(files_blue)
    app.register_blueprint(statement_blue)

    # 配置数据库
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:651748264Zz*@localhost/travelindustry'

    # 初始化插件
    init_exts(app=app)

    return app
