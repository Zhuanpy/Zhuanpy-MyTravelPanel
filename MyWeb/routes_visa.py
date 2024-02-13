from flask import Blueprint, render_template, request
from Visa.Korea.KoreavisaFun import fill_korea_visa_form, create_korea_visa_folder
from Visa.TaiwanVisa import TaiwanVisa

# 创建蓝图
bp = Blueprint('visa_routes', __name__)


@bp.route('/visa_Korea')
def visa_Korea():
    return render_template('visas/korea.html')


# @bp.route('/visa_Korea_form', methods=['POST'])
# def visa_korea_form():
#     if request.method == 'POST':
#         text = request.form['input_folder']
#         print(text)
#     return render_template('VisaHtml/visaKorea.html')


@bp.route('/visaJapan', methods=['GET', 'POST'])
def visa_Japan():
    return render_template('route2.html')


@bp.route('/visaTaiwan', methods=['GET', 'POST'])
def visa_Taiwan():
    return render_template('route2.html')


@bp.route('/visaUs', methods=['GET', 'POST'])
def visa_Us():
    return render_template('route2.html')


# China visa,
@bp.route('/visaChina', methods=['GET', 'POST'])
def visa_China():
    return render_template('route2.html')


# Australia visa ,
@bp.route('/visaAustralia', methods=['GET', 'POST'])
def visa_Australia():
    return render_template('route2.html')


# Malaysia visa
@bp.route('/visaMalaysia', methods=['GET', 'POST'])
def visa_Malaysia():
    return render_template('route2.html')


# uk visa
@bp.route('/visaUk', methods=['GET', 'POST'])
def visa_Uk():
    return render_template('route2.html')
