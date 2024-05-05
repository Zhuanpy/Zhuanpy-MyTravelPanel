from datetime import datetime
from FlightTicket.ConvertFlight.flight_utils import MysqlTravelData


def convert_date_format(original_date: str):
    """ 月份名称 字典映射 """
    month_mapping = {'JAN': '01', 'FEB': '02', 'MAR': '03',
                     'APR': '04', 'MAY': '05', 'JUN': '06',
                     'JUL': '07', 'AUG': '08', 'SEP': '09',
                     'OCT': '10', 'NOV': '11', 'DEC': '12'}

    try:
        # 解析原始日期字符串
        parsed_date = datetime.strptime(original_date, '%d%b')
        # 获取月份名称对应的数字
        M = parsed_date.strftime('%b').upper()
        month_number = month_mapping[M]

        # 格式化为新的日期字符串
        D = parsed_date.strftime('%d')
        new_date_str = f'{month_number}月{D}号'

        return new_date_str

    except ValueError:
        return "无效的日期格式"


def transfer2airport(code3: str):
    # 连接数据库
    connection = MysqlTravelData.connection()

    try:

        with connection.cursor() as cursor:

            # 执行查询
            sql = f"SELECT * FROM airport_data WHERE 机场三字码 = '{code3}'"
            cursor.execute(sql)
            result = cursor.fetchone()
            # result = ('北京', 'PEK', 'ZBAA', '北京首都国际机场', 'BEIJING')
            if result:
                results = (result[0], result[3], result[4])

            else:
                results = None

    finally:
        connection.close()

    return results


def organize_text(texts):
    """
    # text：
    #  1. MU  568 S  05AUG SINPVG HK1  1635   2205  O*       E SA  1
    #  2. MU 6561 B  06AUG PVGHRB HK1  0755   1050  O*       E SU  1
    #  3. FM 9062 B  13AUG HRBPVG HK1  1745   2100  O*         SU  2
    #  4. MU  543 V  13AUG PVGSIN HK1  2350  #0525  O*       E SU  2
    """

    lines = texts.split('\n')

    lis = []

    for i in lines:
        if len(i) < 10:
            continue
        li = i.split(' ')

        try:
            while True:
                li.remove("")

        except ValueError:
            pass

        if len(li) > 10:

            li[5] = f'{li[5][:3]} - {li[5][-3:]}'

            if len(li[7]) == 5:
                li[7] = f'{li[7][:3]}:{li[7][-2:]}'

            else:
                li[7] = f'{li[7][:2]}:{li[7][-2:]}'

            if len(li[8]) == 5:
                li[8] = f'{li[8][:3]}:{li[8][-2:]}'

            else:
                li[8] = f'{li[8][:2]}:{li[8][-2:]}'

        if len(li[2]) < 4:
            str1 = ''
            str2 = ' '
            for i in range(4 - len(li[2])):
                str1 = f'{str2}{str1}'

            li[2] = f'{str1}{li[2]}'

        lis.append(li)

    return lis


def translate_text(texts, language='CN', luggage=None, price=None):
    lis = organize_text(texts)

    itn = ''

    for li in lis:
        iti_num = li[0]  # 1.
        air_code = li[1]  # MF
        flight_code = li[2]  # 860
        departure_date = li[4]

        airport_code = li[5]
        dep_code = airport_code[:3]
        dep_code = transfer2airport(dep_code)

        time_departure = li[7]
        time_arrival = li[8]

        arr_code = airport_code[-3:]
        arr_code = transfer2airport(arr_code)

        if language == 'EN':
            itn1 = f"{iti_num}{dep_code[2]} - {arr_code[2]},  Flight No: {air_code}{flight_code},\n" \
                   f"  {departure_date}, Departure: {time_departure} - Arrival: {time_arrival}\n\n"

        else:
            departure_date = convert_date_format(departure_date)  # 将日期转换为中文；
            itn1 = f"{iti_num}{dep_code[0]} - {arr_code[0]},  航班号：{air_code}{flight_code}，\n" \
                   f"  {departure_date}， 出发： {time_departure} - 抵达：{time_arrival}\n\n"

        itn = f'{itn}{itn1}'

    if language == 'EN':
        itn = f'{itn}Fare: {price}; \nLuggage: {luggage};'

    else:
        itn = f'{itn}票价:  {price}; \n行李: {luggage};'
        # 票价: SGD1180 ，  行李20KG
    return itn


if __name__ == "__main__":
    # # 使用示例
    SIN = 'PEK'
    r = transfer2airport(SIN)
    print(r)
