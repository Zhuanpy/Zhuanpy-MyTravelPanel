from flask import Flask, render_template
from code.routes_visa import bp as visa_routes
from code.route_flight import fb as flight_routes
from code.routes_files import fpb as files_routes
from code.routes_statement import sb as statement_routes

app = Flask(__name__)

app.register_blueprint(visa_routes)
app.register_blueprint(flight_routes)
app.register_blueprint(files_routes)
app.register_blueprint(statement_routes)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/visa')
def visa():
    return render_template('visa.html')


@app.route('/flight')
def flight():
    return render_template('flight.html')


@app.route('/accommodation')
def accommodation():
    return render_template('package.html')


@app.route('/file_processing', methods=['GET', 'POST'])
def file_processing():
    return render_template('files/pdf.html')


@app.route('/statement_uob_processing')
def statement_uob():
    return render_template("statement/UobBank.html")


@app.route('/my_test')
def my_test():
    return render_template("Test.html")


if __name__ == '__main__':
    app.run(debug=True)
