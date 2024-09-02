# from flask import Flask, render_template
# from code.routes_visa import bp as visa_routes
# from code.route_flight import fb as flight_routes
# from code.routes_files import fpb as files_routes
# from code.routes_statement import sb as statement_routes

# app = Flask(__name__)

# app.register_blueprint(visa_routes)
# app.register_blueprint(flight_routes)
# app.register_blueprint(files_routes)
# app.register_blueprint(statement_routes)

from flask import Blueprint, render_template

dex = Blueprint("index", __name__)
@dex.route('/')
def index():
    return render_template('index.html')


@dex.route('/visa')
def visa():
    return render_template('visa.html')


@dex.route('/flight')
def flight():
    return render_template('flight.html')


@dex.route('/accommodation')
def accommodation():
    return render_template('package.html')


@dex.route('/file_processing', methods=['GET', 'POST'])
def file_processing():
    return render_template('files/pdf.html')


@dex.route('/statement_uob_processing')
def statement_uob():
    return render_template("statement/UobBank.html")


@dex.route('/my_test')
def my_test():
    return render_template("Test.html")


# if __name__ == '__main__':
    # app.run(debug=True)
