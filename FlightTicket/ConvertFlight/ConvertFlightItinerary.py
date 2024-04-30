import tkinter as tk
from datetime import datetime
import pandas as pd


def convert_date_format(original_date: str):

    # 月份名称映射字典
    month_mapping = {
        'JAN': '01',
        'FEB': '02',
        'MAR': '03',
        'APR': '04',
        'MAY': '05',
        'JUN': '06',
        'JUL': '07',
        'AUG': '08',
        'SEP': '09',
        'OCT': '10',
        'NOV': '11',
        'DEC': '12'
    }

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


def transfer2airport(SIN: str):
    
    import os
    _path = "E:\Python\Project\MyTravelPanel\FlightTicket\ConvertFlight"
    df = pd.read_csv(f'{_path}/airport_data.csv')
    df = df[df['机场三字码'] == SIN]
    if df.shape:
        city = df['城市名'].values[0]
        cn_airport = df['机场名称'].values[0]
        en_airport = df['英文名称'].values[0]
        results = (city, cn_airport, en_airport)

    else:
        results = None

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


class FlightConvertApp:

    def __init__(self, master):

        self.master = master
        self.master.title("机票行程转化")

        self.label_a = tk.Label(master, text="输入行程")
        self.label_a.pack()

        self.text_frame_a = tk.Frame(master, padx=10, pady=5)
        self.text_frame_a.pack()

        self.text_entry_a = tk.Text(self.text_frame_a, height=8, width=65, wrap=tk.WORD)
        self.text_entry_a.pack()

        self.label_result = tk.Label(master, text="输出行程")
        self.label_result.pack()

        self.text_frame_output = tk.Frame(master, padx=10, pady=5)
        self.text_frame_output.pack()

        self.text_output = tk.Text(self.text_frame_output, height=18, width=65, wrap=tk.WORD, state=tk.NORMAL)
        self.text_output.pack()

        self.result_var = tk.StringVar()
        self.result_var.set("Result B")  # 默认选择结果B

        self.result_b_radio = tk.Radiobutton(master, text="中文行程", variable=self.result_var, value="中文行程")
        self.result_b_radio.pack()

        self.result_c_radio = tk.Radiobutton(master, text="英文行程", variable=self.result_var, value="英文行程")
        self.result_c_radio.pack()

        self.convert_button = tk.Button(master, text="  转 化  ", command=self.convert_text)
        self.convert_button.pack()

    def convert_text(self):

        input_text = self.text_entry_a.get("1.0", "end-1c")
        selected_result = self.result_var.get()

        if selected_result == "中文行程":
            converted_text = translate_text(input_text, 'CN')

        elif selected_result == "英文行程":
            converted_text = translate_text(input_text, 'EN')

        else:
            converted_text = "Invalid result selection"

        self.text_output.delete("1.0", "end")
        self.text_output.insert("1.0", converted_text)


if __name__ == "__main__":
    # root = tk.Tk()
    # app = FlightConvertApp(root)
    # root.mainloop()
    r = transfer2airport('SIN')
    print(r)
