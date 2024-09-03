from flask import Blueprint, render_template
from .code.BankAccout.Statement import OriginalStatement

# 创建蓝图
statement_blue = Blueprint('statement_routes', __name__)


@statement_blue.route('/uob_bank_processing')
def uob_bank_processing():
    st = OriginalStatement()
    st.statement_process()
    print("st.statement_process()")
    return render_template('statement/UobBank.html')


@statement_blue.route('/uob_original_processing')
def uob_original_processing():
    statement = OriginalStatement()
    statement.organized_statement_data()
    print("statement.organized_statement_data()")
    return render_template('statement/UobBank.html')


@statement_blue.route('/latest_company_statement')
def latest_company_statement():
    statement = OriginalStatement()
    statement.latest_company_statement()
    print("statement.organized_statement_data()")
    return render_template('statement/UobBank.html')


@statement_blue.route('/latest_self_statement')
def latest_self_statement():
    statement = OriginalStatement()
    statement.latest_self_statement()
    print("statement.latest_self_statement()")
    return render_template('statement/UobBank.html')


@statement_blue.route('/statement_to_company')
def statement_to_company():
    statement = OriginalStatement()
    statement.statement_to_company()
    print("statement.statement_to_company()")
    return render_template('statement/UobBank.html')
