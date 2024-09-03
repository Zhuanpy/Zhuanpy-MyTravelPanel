from flask import Blueprint, render_template
from .models import *

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
