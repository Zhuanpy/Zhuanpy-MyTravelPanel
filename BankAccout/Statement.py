import os
import pandas as pd

pd.set_option('display.max_columns', None)


class OriginalStatement:

    def __init__(self):
        self.file_path = os.path.join("E:/", "WORKING", "B-账单", "ZHANG ZHUAN UOB MASTER")

    def read_original_file(self):
        original_path = os.path.join(self.file_path, "原始下载")

        files = os.listdir(original_path)

        original_files = [file for file in files if file.endswith('.xls')]

        data = pd.DataFrame()

        for f in original_files:
            file_path = os.path.join(original_path, f)
            df = pd.read_excel(file_path, sheet_name="Sheet0", skiprows=7, engine='xlrd')
            data = pd.concat([data, df])

        data = data.rename(columns={"Available Balance": "Balance",
                                    "Transaction Description": "Description",
                                    "Transaction Date": "T-Date"})

        data["T-Date"] = pd.to_datetime(data["T-Date"]).dt.date

        data["Id"] = data["Description"].astype(str) + data["Balance"].astype(str)
        data["Id"] = data["Id"].str.replace('[\s\.\\/]', '', regex=True).str[-20:].str.lower()

        # 去除重复数据
        data = data.drop_duplicates(subset=["Id"]).reset_index(drop=True)

        return data

    def read_key_word(self, fies: str):
        keyword_path = os.path.join(self.file_path, "原始下载", "Keywords")
        p = os.path.join(keyword_path, f"{fies}.txt")
        f = open(p, 'r')
        keys = []
        for line in f.readlines():
            line = line.replace('\n', '')
            keys.append(line)

        keys = list(set(keys))  # 去重复元素
        return keys

    def key_words_data(self, data):

        use_by_myself = self.read_key_word("keyword_use_by_myself")  # ["PAYNOW-FAST", "MIXUE", "BUS/MRT"]

        use_by_business = self.read_key_word("keyword_use_use_by_business")

        keywords = use_by_myself + use_by_business
        keywords = list(set(keywords))

        def extract_keywords(row):
            text = row["Description"]
            found_keywords = [keyword for keyword in keywords if keyword in text]
            return ', '.join(found_keywords) if found_keywords else None

        # 应用函数并创建新列 D
        data['Keyword'] = data.apply(extract_keywords, axis=1)

        data.loc[data['Keyword'].isin(use_by_myself), 'User'] = 'Me'
        data.loc[data['Keyword'].isin(use_by_business), 'User'] = 'COM'

        return data

    def organized_statement_data(self):

        original = self.read_original_file()

        original["T-Date"] = pd.to_datetime(original["T-Date"]).dt.date
        original = original.sort_values(by=["T-Date"])

        original[["Keyword", "User", "EO", "Credit date"]] = None

        columns = ["T-Date", "Withdrawal", 'Deposit', "EO", "Credit date", "Keyword", "User", "Id", "Description"]

        original = original[columns]

        # 去除转入数据
        original = original[original["Withdrawal"] != 0]

        # 去除转入数据
        original = original.drop(columns=['Deposit'])  # .reset_index(drop=True)
        original = original.dropna(subset=['Description']).reset_index(drop=True)

        # 提取 & 添加关键字列
        original = self.key_words_data(original)

        """ 筛选数据 """
        previous_path = os.path.join(self.file_path, "整理下载", "整理下载.xls")
        previous = pd.read_excel(previous_path, sheet_name="Sheet1", engine='openpyxl')
        previous["T-Date"] = pd.to_datetime(previous["T-Date"]).dt.date
        previous["Credit date"] = pd.to_datetime(previous["Credit date"]).dt.date

        latest_statement = original[~original["Id"].isin(previous["Id"])]

        if latest_statement.empty:
            print("无最整理账单；")

        else:
            latest_statement = pd.concat([previous, latest_statement])
            latest_statement.to_excel(previous_path, index=False, engine='openpyxl')

        return latest_statement

    def latest_company_statement(self):

        """ 读取 statement """
        latest_path = os.path.join(self.file_path, "整理下载", "整理下载.xls")
        statement = pd.read_excel(latest_path, sheet_name="Sheet1", engine='openpyxl')
        statement = statement[(statement["EO"] != "Na") &
                              (statement["User"] == "COM") &
                              (~statement["EO"].isnull())]

        statement["T-Date"] = pd.to_datetime(statement["T-Date"]).dt.date
        statement["Credit date"] = pd.to_datetime(statement["Credit date"]).dt.date

        """ 以前数据 """
        previous_path = os.path.join(self.file_path, "最新账单", "Company", "最新公司账单.xls")
        previous = pd.read_excel(previous_path, sheet_name="Sheet1", engine='openpyxl')
        previous["T-Date"] = pd.to_datetime(previous["T-Date"]).dt.date
        previous["Credit date"] = pd.to_datetime(previous["Credit date"]).dt.date

        """ 最新 statement """
        latest_statement = statement[~statement["Id"].isin(previous["Id"])]

        if latest_statement.empty:
            print("无最新公司账单;")
            return latest_statement

        # 保存 Excel 文件之前设置选项
        latest_statement = pd.concat([previous, latest_statement])
        latest_statement.to_excel(previous_path, index=False, engine='openpyxl')
        print("最新公司账单已更新;")
        return latest_statement

    def latest_self_statement(self):

        """ 读取 statement """
        latest_path = os.path.join(self.file_path, "整理下载", "整理下载.xls")
        statement = pd.read_excel(latest_path, sheet_name="Sheet1", engine='openpyxl')
        statement["T-Date"] = pd.to_datetime(statement["T-Date"]).dt.date
        statement["Credit date"] = pd.to_datetime(statement["Credit date"]).dt.date

        statement = statement[(statement["EO"] == "Na") &
                              (statement["User"] != "COM") &
                              (~statement["EO"].isnull())]

        """ 以前已经整理 statement """
        self_path = os.path.join(self.file_path, "最新账单", "个人账单", "最新个人账单.xls")
        previous = pd.read_excel(self_path, sheet_name="Sheet1", engine='openpyxl')
        previous["T-Date"] = pd.to_datetime(previous["T-Date"]).dt.date
        previous["Credit date"] = pd.to_datetime(previous["Credit date"]).dt.date

        """ 最新 statement """
        latest_statement = statement[~statement["Id"].isin(previous["Id"])]
        if latest_statement.empty:
            print("无最新个人账单;")

        else:
            # 保存 Excel 文件之前设置选项
            latest_statement = pd.concat([previous, latest_statement])
            latest_statement.to_excel(self_path, index=False, engine='openpyxl')
            print("最新个人账单已更新;")

        return latest_statement

    def statement_to_company(self):
        latest_path = os.path.join(self.file_path, "最新账单", "Company", "最新公司账单.xls")
        latest_statement = pd.read_excel(latest_path, sheet_name="Sheet1", engine='openpyxl')

        to_path = os.path.join(self.file_path, "最新账单", "Toboss", "ToCompany.xls")
        to_company_statement = pd.read_excel(to_path, sheet_name="Sheet1", engine='openpyxl')

        latest_statement = latest_statement[~latest_statement["EO"].isin(to_company_statement["EO"])]

        if latest_statement.empty:
            print("无最新公司账单;")

        else:
            latest_statement = latest_statement[["T-Date", "Credit date", "EO", "Withdrawal", "Description"]]
            latest_statement["status"] = "pending"
            latest_statement = pd.concat([to_company_statement, latest_statement])
            latest_statement["T-Date"] = latest_statement["T-Date"].dt.date
            latest_statement["Credit date"] = latest_statement["Credit date"].dt.date

            latest_statement.to_excel(to_path, index=False, engine='openpyxl')

        return latest_statement

    def statement_to_boss(self):

        """存储一份给老板"""
        load_path = os.path.join(self.file_path, "最新账单", "Toboss", "ToCompany.xls")
        statement = pd.read_excel(load_path, sheet_name="Sheet1", engine='openpyxl')
        statement = statement[statement["status"] == "pending"].reset_index(drop=True)
        statement["T-Date"] = statement["T-Date"].dt.date
        statement["Credit date"] = statement["Credit date"].dt.date

        last_date = statement.iloc[-1]["T-Date"]

        Withdrawal_sum = statement["Withdrawal"].sum()
        text = f"Grand Total SGD：{Withdrawal_sum}; "
        statement.loc[len(statement)] = pd.Series(dtype='object')  # 在 DataFrame 最后插入一个空白行
        statement.loc[len(statement), "EO"] = text  # 在空白行后插入说明文字

        # 保存文件
        file_name = f"ZHANG ZHUAN UOB_{last_date}.xls"
        path = os.path.join(self.file_path, "最新账单", "Toboss", file_name)
        statement.to_excel(path, index=False, engine='openpyxl')
        print("To boss账单已更新;")

    def statement_process(self):

        self.organized_statement_data()  # 原始账单整理

        self.latest_company_statement()  # 公司账单整理

        self.latest_self_statement()  # 个人账单整理

        self.statement_to_company()  # 给公司账单

        self.statement_to_boss()  # 发送给老板账单


if __name__ == '__main__':
    uob = OriginalStatement()
    uob.statement_process()
