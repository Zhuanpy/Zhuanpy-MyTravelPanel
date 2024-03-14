from flask import Blueprint, render_template, request
from Visa.Korea.KoreavisaFun import fill_korea_visa_form, create_korea_visa_folder
from Visa.TaiwanVisa import TaiwanVisa

# 创建蓝图
bp = Blueprint('visa_routes', __name__)


# @bp.route('/visa_Korea_create_project', methods=['GET', 'POST'])
# def visa_Korea_create_project():
#
#     if request.method == 'POST':
#         file_name = request.form.get('createproject')
#
#         if file_name:
#             create_korea_visa_folder(file_name)
#
#     return render_template('visas/korea.html')


@bp.route('/visaKoreaPage', methods=['GET', 'POST'])
def visa_Korea_page():
    return render_template('visas/korea.html')


@bp.route('/visaKoreaProcessing', methods=['POST'])
def visa_Korea_processing():
    submit_button = request.form.get('submit_button')

    if submit_button == 'create_project':
        file_path = request.form.get("path_create_project")
        create_korea_visa_folder(file_path)

    elif submit_button == 'fill_form':
        file_path = request.form.get("path_fill_form")
        fill_korea_visa_form(file_path)

    else:
        print('Invalid request')
        # return 'Invalid request'

    return render_template('visas/korea.html')


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
