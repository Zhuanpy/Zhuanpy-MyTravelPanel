import time
import pymysql


def get_times():
    """
    get time
    """
    str_time = time.strftime('%Y{}%m{}%d{} %X')
    str_time = str_time.format('年', '月', '日')
    return str_time


# 假设有10个航班信息

class FlightData:
    # 数据库连接信息
    db_config = {
        'user': 'root',
        'password': '651748264Zz*',
        'host': 'localhost',
        'database': 'traveldata'
    }

    @classmethod
    def athina_booking_code(cls, num, flight, flight_date):

        try:
            # 航班时刻表数据
            flight = flight.replace(" ", "")
            air_code = flight[:2]
            flight_num = flight[2:]
            id_ = air_code + flight_num
            conn = pymysql.connect(**cls.db_config)
            cursor = conn.cursor()

            # 定义查询语句
            query = "SELECT * FROM flight_timing_data WHERE 航班ID = %s"
            # 执行查询
            cursor.execute(query, (id_,))

            # 获取查询结果
            data = cursor.fetchone()

            # 关闭游标和连接
            cursor.close()
            conn.close()

            city = data[3].split(" ")
            city = [item for item in city if item != ""]
            timings = data[4].split(" ")
            timings = [item for item in timings if item != ""]

            departure_city = city[0]
            arrive_city = city[1]
            departure_timing = timings[0]
            arrive_timing = timings[1]

            flight_num = flight_num.rjust(4)  # 补 齐4位数
            arrive_timing = arrive_timing.rjust(5)

            result = (f" {num}. {air_code} {flight_num} Y  "
                      f"{flight_date} {departure_city}{arrive_city} HK1  "
                      f"{departure_timing}  {arrive_timing}  O        E FR")

            return result

        except pymysql.MySQLError as e:
            # 捕获并返回数据库错误
            return f"Database error: {e}"

        except Exception as e:
            # 捕获并返回其他错误
            return f"An error occurred: {e}"

    @classmethod
    def insert_flight(cls, airline: str, flight_number: str, origin: str, departure_time: str, ):

        conn = pymysql.connect(**cls.db_config)
        cursor = conn.cursor()

        try:
            insert_query = '''
                INSERT INTO flight_timing_data (航班ID, 航司, 航班号, 起始城市, 起始时间)
                VALUES (%s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    航司 = VALUES(航司),
                    航班号 = VALUES(航班号),
                    起始城市 = VALUES(起始城市),
                    起始时间 = VALUES(起始时间) '''

            id_ = airline + flight_number
            cursor.execute(insert_query, (id_, airline, flight_number, origin, departure_time))

            conn.commit()

        finally:
            conn.close()


if __name__ == '__main__':
    # 读取 Excel 文件
    file_path = 'E:/WORKING/A-AIR_TICKET/01_FLIGHT/航班时刻表数据.xls'
