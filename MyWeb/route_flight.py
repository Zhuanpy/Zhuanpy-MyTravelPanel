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
    return render_template('flights/Flight_booking_to_Athina.html', flights=flight.usual_flight_list())


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
    return render_template('flights/athina.html', flights=flight.usual_flight_list())


@fb.route('/athinaResult', methods=['POST'])
def results_athina_page():
    # 获取选择内容
    # 将选择内容处理想要的结果
    flight_inform = request.form['flight-info']
    flight_date = request.form['date-info']
    # print(flight_inform)
    # print(flight_date)

    flight_index = request.form['flight-info']
    airline_code = request.form['flight-info']
    flight_number = request.form['flight-info']

    airport_code_departure = request.form['flight-info']
    airport_code_arrival = request.form['flight-info']
    flight_time_departure = request.form['flight-info']
    flight_time_arrival = request.form['flight-info']

    results = f"{flight_index}. {airline_code} {flight_number} y  {flight_date} " \
              f"{airport_code_departure}{airport_code_arrival} Hk1  " \
              f"{flight_time_departure}   {flight_time_arrival}  O        E MO"

    return results


""" 航班信息录入"""


@fb.route('/enterFlightInformation')
def enter_flight_information():
    return render_template('flights/enter_flight_information.html')


# 处理表单提交
@fb.route('/submitFlightInformation', methods=['POST'])
def submit_flight_information():
    airline_code = request.form['airline_code']
    flight_number = request.form['flight_number']
    departure_airport = request.form['departure_airport']
    arrival_airport = request.form['arrival_airport']
    departure_time = request.form['departure_time']
    arrival_time = request.form['arrival_time']

    # 检查航班是否已存在
    csv_file = "E:/Python/Project/MyTravelPanel/FlightTicket/data/flight-information.csv"
    print(f"flight_number: {flight_number}")
    if flight.flight_exists(csv_file, flight_number):
        return render_template('flights/results.html', text="Flight information exist")

    # 添加航班信息到CSV文件
    flight_data = {
        'AIRLINE CODE': airline_code,
        'FLIGHT NUMBER': flight_number,
        'DEPARTURE AIRPORT': departure_airport,
        'ARRIVAL AIRPORT': arrival_airport,
        'DEPARTURE TIME': departure_time,
        'ARRIVAL TIME': arrival_time
    }
    # 新数据添加到csv中；
    flight.add_flight_to_csv(csv_file, flight_data)

    return render_template('flights/results.html', text="Flight information added successfully!")


@fb.route('/flightEntryPage')
def entry_flight_page():
    return render_template('flights/flight_timing_entry.html')


@fb.route('/entryFlightSubmit', methods=['POST'])
def entry_flight_processing():
    air_number = request.form['flight_number']
    air_number = air_number.replace(' ', '')
    airline = air_number[:2]
    flight_number = air_number[2:]

    origin = request.form['origin']
    departure_time = request.form['departure_time']
    print(f"airline:{airline}, flight_number:{flight_number}, origin:{origin}, departure_time:{departure_time}")
    flight.insert_flight(airline, flight_number, origin, departure_time)

    return '新记录插入成功'


if __name__ == '__main__':
    import pandas as pd
    import os

    # 获取当前脚本的路径
    current_path = os.path.dirname(os.path.abspath(__file__))

    CSV_FILE = "E:/Python/Project/MyTravelPanel/FlightTicket/data/flight-information.csv"
    data = pd.read_csv(CSV_FILE)
    # print(data)
    # pass
