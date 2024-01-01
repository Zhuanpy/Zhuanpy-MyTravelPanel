from pathlib import Path
import pandas as pd


class TaiwanVisa:

    def __init__(self, hid, name, path_="E:/WORKING/A-AIR_TICKET"):
        self.hid = hid
        self.name = name
        self.path_ = path_
        self.read_path = ''

    def create_folder(self):
        # 创建嵌套文件夹
        # CHN_VISA_HID155653_HO JIA AI VIVI
        folder = f'TWD_VISA_HID{self.hid}_{self.name}'
        path = Path(f'{self.path_}/{folder}')
        path.mkdir(parents=True)

    def create_request_list(self):
        df = pd.read_excel(self.read_path)
        pass


if __name__ == '__main__':
    tw = TaiwanVisa(123645, 'LILI')
    tw.create_folder()
    tw.create_request_list()
