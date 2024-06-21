import time
import csv
import os
import pandas as pd


def get_times():
    """
    get time
    """
    str_time = time.strftime('%Y{}%m{}%d{} %X')
    str_time = str_time.format('年', '月', '日')
    return str_time


# 假设有10个航班信息

class FlightData:
    flight_data_path = os.path.join("E:", "/WORKING", "A-AIR_TICKET", "01_FLIGHT")

    @classmethod
    def usual_flight_list(cls):
        flight_list = []
        return flight_list

    @classmethod
    def create_csv(cls, csv_file):
        """ 创建CSV文件头部 """
        with open(csv_file, 'w', newline='') as csvfile:
            fieldnames = ['AIRLINE CODE', 'FLIGHT NUMBER', 'DEPARTURE AIRPORT', 'ARRIVAL AIRPORT', 'DEPARTURE TIME',
                          'ARRIVAL TIME']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

    @classmethod
    def flight_exists(cls, csv_file, flight_number):
        """ 检查航班是否已经存在 """

        with open(csv_file, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['FLIGHT NUMBER'] == flight_number:
                    return True
        return False

    @classmethod
    def add_flight_to_csv(cls, CSV_FILE, data):
        """ 添加航班信息到CSV文件 """
        with open(CSV_FILE, 'a', newline='') as csvfile:
            fieldnames = ['AIRLINE CODE', 'FLIGHT NUMBER', 'DEPARTURE AIRPORT', 'ARRIVAL AIRPORT', 'DEPARTURE TIME',
                          'ARRIVAL TIME']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(data)

    @classmethod
    def athina_booking_code(cls, num, flight, flight_date):
        flight = flight.replace(" ", "")

        air_code = flight[:2]
        flight_num = flight[2:]

        # 航班时刻表数据.xls
        data_path = os.path.join(cls.flight_data_path, "航班时刻表数据.xls")

        try:
            data = pd.read_excel(data_path, sheet_name="Sheet1", dtype={"航班号": str})

        except Exception as e:
            return f"Error reading Excel file: {e}"

        filtered_data = data[(data["航司"] == air_code) & (data["航班号"] == flight_num)]

        if filtered_data.empty:
            return "No matching flight data found."

        try:
            city = filtered_data["起始城市"].values[0].split(" ")
            timings = filtered_data["起始时间"].values[0].split(" ")
        except IndexError as e:
            return f"Error processing data: {e}"

        if len(city) < 2 or len(timings) < 2:
            return "Invalid data format in the Excel file."

        departure_city = city[0]
        arrive_city = city[1]
        departure_timing = timings[0]
        arrive_timing = timings[1]

        flight_num = flight_num.rjust(4)  # 补齐4位数
        arrive_timing = arrive_timing.rjust(5)

        result = (f" {num}. {air_code} {flight_num} Y  "
                  f"{flight_date} {departure_city}{arrive_city} HK1  "
                  f"{departure_timing}  {arrive_timing}  O        E FR")

        # result = (f"{num}. {air_code} {flight_num} Y {flight_date} "
        #           f"{departure_city}{arrive_city} HK1 {departure_timing} "
        #           f"{arrive_timing}  O        E FR")

        return result


if __name__ == '__main__':
    num, flight, flight_date = "1", "TR189", "10JUN"
    f = FlightData()
    r = f.athina_booking_code(num, flight, flight_date)
    print(r)
