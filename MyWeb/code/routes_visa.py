from flask import Blueprint, render_template, request
from Visa.Korea.KoreavisaFun import KoreaVisa
from Filefloder import CreateVisaFolder as cvf


# 创建蓝图
bp = Blueprint('visa_routes', __name__)


@bp.route('/visaKoreaPage', methods=['GET', 'POST'])
def visa_Korea():
    return render_template('visas/korea.html')


@bp.route('/visaKoreaProcessing', methods=['POST'])
def visa_Korea_processing():
    submit_button = request.form.get('submit_button')

    if submit_button == 'create_project':
        file_path = request.form.get("path_create_project")
        cvf.Korea_folder(file_path)

    elif submit_button == 'fill_form':
        file_path = request.form.get("path_fill_form")
        KoreaVisa.fill_form(file_path)

    else:
        print('Invalid request')

    return render_template('visas/result.html')


""" 处理日本签证 """


@bp.route('/visaJapan', methods=['GET', 'POST'])
def visa_Japan():
    return render_template('visas/Japan_visa.html')


@bp.route('/visaJapanProcessing', methods=['POST'])
def visa_Japan_processing():
    file_path = request.form.get("path_create_project")
    cvf.Japan_folder(file_path)

    return render_template('visas/result.html')


""" 处理台湾签证 """


@bp.route('/visaTaiwan', methods=['GET', 'POST'])
def visa_Taiwan():
    return render_template('visas/Taiwan_visa.html')


@bp.route('/visaTaiwanProcessing', methods=['POST'])
def visa_Taiwan_processing():
    file_name = request.form.get("path_create_project")
    cvf.Taiwan_folder(file_name)
    return render_template('visas/result.html')


""" 处理 US 签证 """


@bp.route('/visaUs', methods=['GET', 'POST'])
def visa_Us():
    return render_template('visas/Us_visa.html')


@bp.route('/visaUsProcessing', methods=['GET', 'POST'])
def visa_Us_processing():
    file_name = request.form.get("path_create_project")
    cvf.Us_folder(file_name)
    return render_template('visas/result.html')


""" 处理 China 签证 """


@bp.route('/visaChina', methods=['GET', 'POST'])
def visa_China():
    return render_template('visas/China_visa.html')


@bp.route('/visaChinaProcessing', methods=['GET', 'POST'])
def visa_China_processing():
    file_name = request.form.get("path_create_project")
    cvf.China_folder(file_name)
    return render_template('visas/result.html')


@bp.route('/visaChinaPassport', methods=['GET', 'POST'])
def visa_ChinaPassport():
    return render_template('visas/ChinaPassport.html')


@bp.route('/visaChinaPassportProcessing', methods=['GET', 'POST'])
def visa_ChinaPassport_processing():
    file_name = request.form.get("path_create_project")
    cvf.ChinaPassport_folder(file_name)
    return render_template('visas/result.html')


@bp.route('/visaAustralia', methods=['GET', 'POST'])
def visa_Australia():
    return render_template('visas/Australia_visa.html')


@bp.route('/visaAustraliaProcessing', methods=['GET', 'POST'])
def visa_Australia_processing():
    file_name = request.form.get("path_create_project")
    cvf.Australia_folder(file_name)
    return render_template('visas/result.html')


# Malaysia visa
@bp.route('/visaMalaysia', methods=['GET', 'POST'])
def visa_Malaysia():
    return render_template('visas/Malaysia_visa.html')


@bp.route('/visaMalaysiaProcessing', methods=['GET', 'POST'])
def visa_Malaysia_processing():
    file_name = request.form.get("path_create_project")
    cvf.Malaysia_folder(file_name)
    return render_template('visas/result.html')


# uk visa
@bp.route('/visaUk', methods=['GET', 'POST'])
def visa_Uk():
    return render_template('visas/Uk_visa.html')


@bp.route('/visaUkProcessing', methods=['GET', 'POST'])
def visa_Uk_processing():
    file_name = request.form.get("path_create_project")
    cvf.Uk_folder(file_name)
    return render_template('visas/result.html')


@bp.route('/visaNZL', methods=['GET', 'POST'])
def visa_NewZealand():
    return render_template('visas/NZL_visa.html')


@bp.route('/visaNZLProcesseing', methods=['GET', 'POST'])
def visa_NewZealand_processing():
    file_name = request.form.get("path_create_project")
    cvf.NewZealand_folder(file_name)
    return render_template('visas/result.html')


@bp.route('/visaSchengen', methods=['GET', 'POST'])
def visa_Schengen():
    return render_template('visas/Schengen_visa.html')


@bp.route('/visaSchengenProcesseing', methods=['GET', 'POST'])
def visa_Schengen_processing():
    file_name = request.form.get("path_create_project")
    cvf.Schengen_folder(file_name)
    return render_template('visas/result.html')
