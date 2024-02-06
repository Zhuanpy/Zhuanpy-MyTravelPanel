from flask import Flask, render_template
from Visa.Korea.KoreavisaFun import fill_korea_visa_form, create_korea_visa_folder

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/visaKorea')
def visaKorea():
    return render_template('visaKorea.html')


@app.route('/visa')
def visa():
    return render_template('visa.html')


@app.route('/flight')
def flight():
    return render_template('flight.html')


@app.route('/accommodation')
def accommodation():
    return render_template('package.html')


@app.route('/file_processing')
def file_processing():
    return render_template('file_processing.html')


@app.route('/KoreaVisaProject')
def create_korea_visa_project(file_name):
    create_korea_visa_folder(file_name)
    return ""


if __name__ == '__main__':
    app.run(debug=True)
