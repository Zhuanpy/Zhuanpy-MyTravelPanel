from flask import Blueprint, render_template, request, jsonify
from FlightTicket.ConvertFlight.ConvertFlightItinerary import translate_text
from MyWeb.utils import FlightData as flight

# 创建蓝图
fb = Blueprint('flight_routes', __name__)


# 机票 行程转换
@fb.route('/conversion')
def itinerary_conversion():
    return render_template('flights/conversion.html', output_text="")


@fb.route('/convertPage', methods=['POST'])
def itinerary_convert_process():
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

    return render_template('flights/conversion.html', output_text=output_text)


# Athina 机票订单处理
@fb.route('/athinaPage')
def flight_to_athina_page():
    return render_template('flights/Flight_booking_to_Athina.html')


@fb.route('/process', methods=['POST'])
def flight_to_athina_page_process():
    data = request.json
    itinerary = ""

    num = 1
    for entry in data:
        flight_number = entry.get('flightNumber', '未知航班号')
        flight_date = entry.get('flightDate', '未知日期')

        r = flight.athina_booking_code(num, flight_number, flight_date)
        itinerary += f"{r}\n"
        num += 1

    return jsonify({'itinerary': itinerary})


# 酷航信息输入
@fb.route('/scootPage')
def render_scoot_page():
    return render_template('flights/scoot.html', output_text="")


# Athina  订单处理
@fb.route('/athinaPage')
def render_athina_page():
    return render_template('flights/athina.html')


""" 航班信息录入"""


@fb.route('/enterFlightInformation')
def enter_flight_information():
    return render_template('flights/enter_flight_information.html')


@fb.route('/flightEntryPage')
def entry_flight_page():
    return render_template('flights/flight_timing_entry.html')


@fb.route('/entry_flight_processing', methods=['POST'])
def entry_flight_processing():
    flight_numbers = request.form.getlist('flightNumber[]')
    flight_numbers = [item for item in flight_numbers if item != '']

    origins = request.form.getlist('origin[]')
    origins = [item for item in origins if item != '']

    departure_times = request.form.getlist('departureTime[]')
    departure_times = [item for item in departure_times if item != '']

    if not flight_numbers or not origins or not departure_times:
        return '<div style="text-align: center;">数据插入失败，未输入航班数据</div>'

    flights = [
        {"flightNumber": flight_number, "origin": origin, "departureTime": departure_time}
        for flight_number, origin, departure_time in zip(flight_numbers, origins, departure_times)
    ]

    for f in flights:
        air_number = f['flightNumber']
        origin = f['origin']
        departure_time = f['departureTime']

        air_number = air_number.replace(' ', '')
        airline = air_number[:2]
        flight_number = air_number[2:]
        flight.insert_flight(airline, flight_number, origin, departure_time)

    return '<div style="text-align: center;">新记录插入成功</div>'


if __name__ == '__main__':
    pass
