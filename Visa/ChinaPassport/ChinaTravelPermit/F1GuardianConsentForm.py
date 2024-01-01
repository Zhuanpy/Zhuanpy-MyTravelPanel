import cv2
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os


def nums_files(folder_path):
    # 指定要统计文件数量的文件夹路径
    # folder_path = '/path/to/your/folder'

    # 使用 os.listdir() 获取文件夹中所有文件和子文件夹的列表
    items = os.listdir(folder_path)

    # 使用列表推导式筛选出只是文件而不是文件夹的项
    file_items = [item for item in items if os.path.isfile(os.path.join(folder_path, item))]

    # 获取文件数量
    file_count = len(file_items)
    return file_count


# 获取图片坐标函数
def get_locations(original, temp):  # 获取图片坐标函数

    # 读取大图片和小图片
    large_image = cv2.imread(original)
    small_image = cv2.imread(temp)

    # 使用匹配方法
    result = cv2.matchTemplate(large_image, small_image, cv2.TM_CCOEFF_NORMED)

    # 获取最大匹配位置
    _, _, _, max_loc = cv2.minMaxLoc(result)

    # 打印小图标在大图片中的位置
    return max_loc


def template_locations(folder: str):
    _root = 'E:/WORKING/A-AIR_TICKET/01_Visa/VisaDocumentRequirements/ChinaTravelPassport'
    temppath = f'{_root}/{folder}/template'
    original = f'{_root}/{folder}/FormSample.jpg'

    loc_list = []
    num = nums_files(temppath)  # 统计出文件数量

    for i in range(num):
        f = i + 1

        if f < 10:
            f = f'0{f}.jpg'
        else:
            f = f'{f}.jpg'

        f_name = f'{temppath}/{f}'
        loc = get_locations(original, f_name)
        loc_list.append(loc)

    return loc_list


class TravelPassportFrom:

    def __init__(self):
        self._root_path = 'E:/WORKING/A-AIR_TICKET/01_Visa/VisaDocumentRequirements/ChinaTravelPassport'
        self.file_name = '信息列表.xls'
        self.out_path = 'E:/WORKING/A-AIR_TICKET'

    def inform001_guardian_consent(self, ):
        file = f'{self._root_path}/{self.file_name}'
        df = pd.read_excel(file, sheet_name='Sheet1')
        df = df[['01监护人同意书', '01监护人同意书排序', '类目1', '类目2', '详细']]
        df = df.dropna(subset=['01监护人同意书'])
        inf_list = list(df['详细'])
        return inf_list

    def inform002_declaration_travel_document(self, ):
        file = f'{self._root_path}/{self.file_name}'
        df = pd.read_excel(file, sheet_name='Sheet1')
        df = df[['02申请声明', '02申请声明排序', '类目1', '类目2', '详细']]
        df = df.dropna(subset=['02申请声明'])
        df = df.sort_values(by=['02申请声明排序'])
        inf_list = list(df['详细'])
        return inf_list

    def inform003_noHouseholdRegistration(self, ):
        file = f'{self._root_path}/{self.file_name}'
        df = pd.read_excel(file, sheet_name='Sheet1')

        df = df[['03无户籍声明', '03无户籍声明序列', '类目1', '类目2', '详细']]
        df = df.dropna(subset=['03无户籍声明'])
        df = df.sort_values(by=['03无户籍声明序列'])
        inf_list = list(df['详细'])
        return inf_list

    def edit_form_jpg(self, folder: str, location_list: list, information_list: list):
        image_path = f'{self._root_path}/{folder}/Form.jpg'
        image = Image.open(image_path)
        # 创建一个Draw对象
        draw = ImageDraw.Draw(image)

        # 选择字体,字号,颜色
        font = ImageFont.truetype("simsun.ttc", 50)  # 楷体字体文件
        text_color = (0, 0, 0)  # # 选择文字颜色

        for i in range(len(information_list)):
            texts = str(information_list[i])
            text_position = location_list[i]  # 文字在图片中的位置，以左上角为原点
            # 添加 customer name 到图片
            draw.text(text_position, texts, font=font, fill=text_color)  #

        # 保存修改后的图片
        image.save(f'{self.out_path}/{folder}.jpg')

    def edit001_guardian_consent_inform(self):
        folder = 'F001GuardianConsentForm'
        locations = template_locations(folder)
        information = self.inform001_guardian_consent()
        self.edit_form_jpg(folder, locations, information)

    def edit002_declaration_travel_document_from(self):
        folder = 'F002DeclarationTravelDocument'
        information = self.inform002_declaration_travel_document()
        locations = template_locations(folder)
        self.edit_form_jpg(folder, locations, information)

    def edit003_guardian_consent_inform(self):
        folder = 'F003NoHouseholdRegistration'
        locations = template_locations(folder)
        information = self.inform003_noHouseholdRegistration()
        self.edit_form_jpg(folder, locations, information)

    def my_form(self):
        self.edit001_guardian_consent_inform()
        self.edit002_declaration_travel_document_from()
        self.edit003_guardian_consent_inform()


if __name__ == "__main__":
    form = TravelPassportFrom()
    form.my_form()
    # print(inf_list)
