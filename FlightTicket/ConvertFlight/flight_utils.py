import pymysql
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


class MysqlTravelData:

    db_config = {
        'user': 'root',
        'password': '651748264Zz*',
        'host': 'localhost',
        'database': 'traveldata'
    }

    @classmethod
    def connection(cls):
        connection = pymysql.connect(**cls.db_config)
        return connection


class AthinaBooking:

    @classmethod
    def return_text(cls, airline: str, flight_num: str, dep_airport: str,
                    arr_airport: str, dep_time: str, arr_time: str):
        """
        示例用法结果
        1. TR  124 Y  12MAY SINCSX HS1  1805   2250
        """

        r = f"1. {airline}  {flight_num} E  30JUN {dep_airport}{arr_airport} HS1  {dep_time}  {arr_time} "
        return r


def download_airport_code():

    for i in range(10, 290):
        url = f'https://airportcode.bmcx.com/{i}__airportcode/'
        response = requests.get(url)
        # if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # 找到包含机场信息的表格
        airport_table = soup.find('table')
        # 遍历表格行
        airport_df = pd.read_html(str(airport_table), header=0)
        airport_df = airport_df[1]

        # 保存为CSV文件
        airport_df.to_csv('airport_data.csv', mode='a', header=False, index=False)
        time.sleep(4)

    return True


def append_airport_data(city_cn: str, code3: str, code4: str, airport_name_cn: str, airport_name_en: str):
    """ 添加新机场数据到数据库
    Args:
        city_cn (str): 中文城市名
        code3 (str): 三字代码
        code4 (str): 四字代码
        airport_name_cn (str): 中文机场名
        airport_name_en (str): 英文机场名

    Returns:
        bool: 插入是否成功

    示例用法
    append_airport_data('北京', 'PEK', 'ZBAA', '北京首都国际机场', 'Beijing Capital International Airport')
    """

    # 连接数据库
    connection = MysqlTravelData.connection()

    try:
        with connection.cursor() as cursor:
            # 执行插入
            sql = "INSERT INTO airport_data (城市名, 机场三字码, 机场四字码, 机场名称, 英文名称) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (city_cn, code3, code4, airport_name_cn, airport_name_en))

        # 提交事务
        connection.commit()

        return True

    except pymysql.Error as e:
        print(f"Error inserting airport data: {e}")
        return False

    finally:
        # 关闭数据库连接
        connection.close()


if __name__ == '__main__':
    city_cn = "扬州"
    code3 = "YTY"
    code4 = "ZSYA"
    airport_name_cn = "扬泰国际机场"
    airport_name_en = "Yangzhou Taizhou International Airport"
    append_airport_data(city_cn, code3, code4, airport_name_cn, airport_name_en)
