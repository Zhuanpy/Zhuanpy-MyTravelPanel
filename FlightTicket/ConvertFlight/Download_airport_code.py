import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

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
    print(f'290 page: 第{i}页；')
    time.sleep(4)