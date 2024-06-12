import time
import csv


def get_times():
    """
    get time
    """
    str_time = time.strftime('%Y{}%m{}%d{} %X')
    str_time = str_time.format('年', '月', '日')
    return str_time


# 假设有10个航班信息

class FlightData:

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


if __name__ == '__main__':
    flight = FlightData()
    # pass
