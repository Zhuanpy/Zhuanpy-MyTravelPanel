from flask import Blueprint, render_template, request
from FlightTicket.ConvertFlight.ConvertFlightItinerary import translate_text

# 创建蓝图
fb = Blueprint('flight_routes', __name__)


@fb.route('/conversion')
def itinerary_conversion():
    return render_template('flights/conversion.html', output_text="")


@fb.route('/convert', methods=['POST'])
def convert():
    input_text = request.form['input_text']
    language = request.form['language']
    luggage = request.form['luggage']
    price = request.form['price']

    # 根据选择的语言进行文字转换
    output_text = ""

    if language == "chinese":
        # 中文行程转换逻辑
        output_text = translate_text(input_text, luggage=luggage, price=price)

    elif language == "english":
        # 英文行程转换逻辑
        output_text = translate_text(input_text, language='EN', luggage=luggage, price=price)

    print(output_text)
    return render_template('flights/conversion.html', output_text=output_text)
