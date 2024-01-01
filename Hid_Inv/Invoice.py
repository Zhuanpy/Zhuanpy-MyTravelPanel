import pandas as pd
import os

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)


class CountHid:

    def __init__(self):

        self._path = 'E:/WORKING/B-账单/BOOKING'

    def read_all_inv(self, complete_month=0):
        path = os.path.join(self._path, 'Invoice')
        files = os.listdir(path)
        datas = pd.DataFrame()

        for f in files:

            y = f[:6]
            if int(y) < int(complete_month):
                continue

            name = os.path.join(path, f)  # f'{path}/{f}'

            df = pd.read_excel(name, sheet_name='Sheet1', header=None)  # , names=columns)
            df = df.drop(columns=[1, 7, 9, 10, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28])

            df = df.dropna(subset=[0, 2])

            df[[0, 2]] = df[[0, 2]].astype(int)
            df[[3, 5]] = df[[3, 5]].astype(str)

            # 调整日期
            df[3] = df[3].str[2:]
            df[5] = df[5].str[2:]
            df[3] = pd.to_datetime(df[3], format='%d-%m-%y')
            df[5] = pd.to_datetime(df[5], format='%d-%m-%y')

            datas = pd.concat([datas, df], ignore_index=True)

        return datas

    def read_all_hid(self, complete_month=0):
        hid_path = os.path.join(self._path, 'HID')
        hid_files = os.listdir(hid_path)

        datas = pd.DataFrame()

        for f in hid_files:
            y = f[:6]

            if int(y) < int(complete_month):
                continue

            name = os.path.join(hid_path, f)
            df = pd.read_excel(name, sheet_name='Sheet1', header=None)

            # 使用列名而不是列索引，提高代码可读性
            # 注意：如果不确定列名，可以考虑输出 df.columns 看看具体的列名
            df = df.drop(columns=[1, 11, 6, 12, 13, 14, 15])

            # 使用 dropna 处理缺失值，确保删除的是非空值而不是任何值
            df = df.dropna(subset=[0, 2])
            df[0] = df[0].astype(int)
            df[[2, 4]] = df[[2, 4]].astype(str)

            # 调整日期
            df[2] = df[2].str[2:]
            df[4] = df[4].str[2:]
            df[2] = pd.to_datetime(df[2], format='%d-%m-%y')
            df[4] = pd.to_datetime(df[4], format='%d-%m-%y')

            datas = pd.concat([datas, df], ignore_index=True)

        return datas

    def find_no_inv_booking(self, pre_month='2023-05'):
        complete_path = os.path.join(self._path, 'complete.txt')

        with open(complete_path, 'r') as cm_file:
            complete_month = int(cm_file.readline().strip())

        # 读取所有发票和预订信息
        inv = self.read_all_inv(complete_month)
        hid = self.read_all_hid(complete_month)

        #  清除盈利为 0，不正常订单
        hid = hid[~hid[0].isin(list(inv[0]))]
        hid = hid[hid[7] != 0]

        # 清除已经发现有争议订单
        disputed = self.read_disputed()
        hid = hid[~hid[0].isin(disputed)]

        hid = hid.sort_values(by=[0])
        hid = hid.reset_index(drop=True)
        profits = hid[9].sum()
        print(hid.head(20))

        # 获取最新做账进度，做账至几月份，并保存记录
        last_month = hid[2][0].strftime('%Y%m')
        with open(complete_path, 'w') as f:
            f.write('\n'.join([last_month]))

        # 整理前几个月订单
        pre_booking = hid[hid[2] < pd.to_datetime(pre_month)]
        pre_sum = pre_booking[9].sum()

        return profits, pre_sum

    def read_disputed(self):
        disputed_file_path = os.path.join(self._path, 'disputed.txt')
        # 使用 with 语句确保文件正确关闭
        with open(disputed_file_path, 'r') as file:
            data = pd.read_csv(file, header=None, squeeze=True)
        li = data.values
        return li


class CountMonth:

    def __init__(self, start_month=202304, end_month=202307):

        self._path = 'E:/WORKING/B-账单/BOOKING'
        self.start_month = start_month
        self.end_month = end_month

    def import_my_performance(self, ):
        hid_path = os.path.join(self._path, 'HID')
        hid_files = os.listdir(hid_path)
        performance = pd.DataFrame()

        for f in hid_files:

            y = f[:6]

            if int(y) < int(self.start_month) or int(y) > self.end_month:
                continue

            name = os.path.join(hid_path, f)
            df = pd.read_excel(name, sheet_name='Sheet1', header=None)

            df = df.drop(columns=[1, 11, 6, 13, 14, 15])
            df = df.dropna(subset=[12])
            df[0] = df[0].astype(int)
            df[[2, 4]] = df[[2, 4]].astype(str)

            # 调整日期
            df[2] = df[2].str[2:]
            df[4] = df[4].str[2:]

            df[2] = pd.to_datetime(df[2], format='%d-%m-%y')
            df[4] = pd.to_datetime(df[4], format='%d-%m-%y')

            df = df.sort_values(by=[2, 0]).reset_index(drop=True)
            hids = df[0].values
            first_hid = hids[0]
            last_hid = hids[-1]

            df['firstHid'] = first_hid
            df['lastHid'] = last_hid

            performance = pd.concat([performance, df], ignore_index=True)
            performance[2] = pd.to_datetime(performance[2])

            performance = performance.sort_values(by=0)

            performance['month'] = performance[2].dt.strftime('%Y-%m')

        return performance


if __name__ == '__main__':
    # pre = '2023-09'
    # count = CountHid()
    # profit, _sum = count.find_no_inv_booking(pre)
    # print(f'profit: {profit}, pre sum: {_sum}')

    count = CountMonth()
    data = count.import_my_performance()
    print(data)
