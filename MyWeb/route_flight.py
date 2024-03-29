from flask import Blueprint, render_template, request
from FlightTicket.ConvertFlight.ConvertFlightItinerary import translate_text
import csv

# 创建蓝图
fb = Blueprint('flight_routes', __name__)


# 机票 行程转换
@fb.route('/conversion')
def itinerary_conversion():
    return render_template('flights/conversion.html', output_text="")


@fb.route('/convertPage', methods=['POST'])
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


# 酷航信息输入
@fb.route('/scootPage')
def render_scoot_page():
    return render_template('flights/scoot.html', output_text="")


# 假设有10个航班信息
flights = [
    ["新加坡-达卡", "1. 6E 1016 SIN CCU 0415 0600", "2. 6E 1105 CCU DAC 1450 1615"],
    ["新加坡-TRZ", "1. 6E 1016 SIN CCU 0415 0600", "2. 6E 1105 CCU DAC 1450 1615"],
    ["新加坡-MAA", "1. 6E 1016 SIN CCU 0415 0600", "2. 6E 1105 CCU DAC 1450 1615"],
    ["新加坡-DMK", "1. 6E 1016 SIN CCU 0415 0600", "2. 6E 1105 CCU DAC 1450 1615"],
    ["新加坡-CNX", "1. 6E 1016 SIN CCU 0415 0600", "2. 6E 1105 CCU DAC 1450 1615"],
    ["新加坡-达卡", "1. 6E 1016 SIN CCU 0415 0600", "2. 6E 1105 CCU DAC 1450 1615"],
    ["新加坡-达卡", "1. 6E 1016 SIN CCU 0415 0600", "2. 6E 1105 CCU DAC 1450 1615"],
    ["新加坡-达卡", "1. 6E 1016 SIN CCU 0415 0600", "2. 6E 1105 CCU DAC 1450 1615"],
    ["新加坡-达卡", "1. 6E 1016 SIN CCU 0415 0600", "2. 6E 1105 CCU DAC 1450 1615"],
    ["新加坡-达卡", "1. 6E 1016 SIN CCU 0415 0600", "2. 6E 1105 CCU DAC 1450 1615"],
    ["新加坡-达卡", "1. 6E 1016 SIN CCU 0415 0600", "2. 6E 1105 CCU DAC 1450 1615"],
    ["新加坡-达卡", "1. 6E 1016 SIN CCU 0415 0600", "2. 6E 1105 CCU DAC 1450 1615"]
]


# 创建CSV文件头部
def create_csv(CSV_FILE):
    with open(CSV_FILE, 'w', newline='') as csvfile:
        fieldnames = ['AIRLINE CODE', 'FLIGHT NUMBER', 'DEPARTURE AIRPORT', 'ARRIVAL AIRPORT', 'DEPARTURE TIME',
                      'ARRIVAL TIME']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()


# 检查航班是否已经存在
def flight_exists(CSV_FILE, flight_number):
    with open(CSV_FILE, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['FLIGHT NUMBER'] == flight_number:
                return True
    return False


# 添加航班信息到CSV文件
def add_flight_to_csv(CSV_FILE, data):

    with open(CSV_FILE, 'a', newline='') as csvfile:

        fieldnames = ['AIRLINE CODE', 'FLIGHT NUMBER', 'DEPARTURE AIRPORT', 'ARRIVAL AIRPORT', 'DEPARTURE TIME',
                      'ARRIVAL TIME']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(data)


# Athina  订单处理
@fb.route('/athinaPage')
def render_athina_page():
    return render_template('flights/athina.html', flights=flights)


@fb.route('/athinaResult')
def results_athina_page():
    # 获取选择内容
    # 将选择内容处理想要的结果
    flight_index = ""
    airline_code = ""
    flight_number = ""
    flight_date = ""
    airport_code_departure = ""
    airport_code_arrival = ""
    flight_time_departure = ""
    flight_time_arrival = ""

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
    if flight_exists(csv_file, flight_number):
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
    add_flight_to_csv(csv_file, flight_data)
    return render_template('flights/results.html', text="Flight information added successfully!")


if __name__ == '__main__':
    import pandas as pd
    import os

    # 获取当前脚本的路径
    current_path = os.path.dirname(os.path.abspath(__file__))

    CSV_FILE = "E:/Python/Project/MyTravelPanel/FlightTicket/data/flight-information.csv"
    data = pd.read_csv(CSV_FILE)
    # print(data)
    # pass
