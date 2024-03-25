import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from Filefloder import CreateVisaProgram as Program
import os
import time


class KoreaVisa:
    folder_title = "Korea_vsia"
    working_path = Program.working_folder

    @classmethod
    def combine_JPG2Pdf(cls, folderPath: str, pdfFilePath: str):

        folderPath = os.path.join(folderPath, "temp")  # /'

        pdfFilePath = f'{pdfFilePath}/my_form.pdf'

        files = os.listdir(folderPath)
        pngFiles = []
        sources = []

        THRESHOLD_VALUE = 0  # 设定不转化的图片
        for file in files:

            if any(ext in file.lower() for ext in ['jpg', 'png', 'jpeg', 'webp']):
                filename = os.path.splitext(file)[0]

                try:
                    if int(filename) > THRESHOLD_VALUE:
                        pngFiles.append(os.path.join(folderPath, file))
                except ValueError:
                    pngFiles.append(os.path.join(folderPath, file))

        pngFiles.sort()
        output = Image.open(pngFiles[0])
        pngFiles.pop(0)

        for file in pngFiles:

            pngFile = Image.open(file)

            if pngFile.mode == "RGB":
                pngFile = pngFile.convert("RGB")

            sources.append(pngFile)

        output.save(pdfFilePath, "pdf", save_all=True, append_images=sources)

    @classmethod
    def create_visa_folder(cls, file_name: str):

        # 项目资源文件夹
        source_folder = os.path.join(Program.visa_requirements_folder, '01_Korea_vsia', "vsia_form")

        # 项目目标文件夹
        name = f'Korea_vsia_{file_name}'
        destination_folder = os.path.join(Program.working_folder, name)

        Program.copy_folder_contents(source_folder, destination_folder)

        # try:
        #     file_name = file_name.upper()
        #     folder_name = f'KOR_VISA_{file_name}'
        #
        #     folder_path = Path(f'{cls.root_path}/{folder_name}')
        #     folder_path.mkdir(parents=True)
        #
        #     # 创建子文件夹
        #     temp = Path(f'{cls.root_path}/{folder_name}/temp')
        #     temp.mkdir(parents=True)
        #
        #     """ 复制 文档列表 excel """
        #     document_list_source_path = f'{cls.data_path}/DocumentList.xls'
        #     document_list_destination_path = f'{folder_path}/DocumentList.xls'
        #     shutil.copy(document_list_source_path, document_list_destination_path)
        #
        #     """ 复制 表格 excel """
        #     form_source_path = f'{cls.data_path}/FormSample.xls'
        #     form_destination_path = f'{folder_path}/FormSample.xls'
        #     shutil.copy(form_source_path, form_destination_path)
        #
        # except FileExistsError:
        #     pass

    @classmethod
    def fill_form(cls, folder: str):

        destination_folder_name = f'{cls.folder_title}_{folder}'

        destination_file_path = os.path.join(cls.working_path, destination_folder_name)

        source_path = os.path.join(cls.working_path, "01_Visa", "VisaDocumentRequirements", "01_Korea_vsia")

        for p in range(1, 6):

            page = f'PAGE0{p}'

            """ 读取坐标信息 """
            loc_list = pd.read_excel(f'{source_path}/坐标列表.xls', sheet_name='Sheet1')

            loc_list = loc_list[loc_list['PAGE'] == page]
            loc_list[["坐标序列"]] = loc_list[["坐标序列"]].astype(str)
            loc_list[["坐标X", "坐标Y"]] = loc_list[["坐标X", "坐标Y"]].astype(int)

            """  清理填写表格信息 """
            form = pd.read_excel(f'{destination_file_path}/FormSample.xls', sheet_name='Sheet1')

            form = form[form['PAGE'] == page]
            form = form[~(form['DETAIL'].isnull())]

            # form['PAGE'] = form['序列'].astype(int)
            form[["坐标序列", "DETAIL"]] = form[["坐标序列", "DETAIL"]].astype(str)

            image_path = f'{source_path}/Form-page-{p}.jpg'
            image = Image.open(image_path)
            # 创建一个Draw对象
            draw = ImageDraw.Draw(image)
            # 选择字体,字号,颜色
            font = ImageFont.truetype("simsun.ttc", 50)  # 楷体字体文件
            text_color = (0, 0, 255)  # # 选择文字颜色

            for i in form.index:
                filling_texts = form.loc[i, 'DETAIL']  # str(form.loc[i, 'DETAIL'])
                form_type = form.loc[i, '类型']
                filling_Number = form.loc[i, '坐标序列']

                if form_type == "选择":
                    filling_Number = filling_Number + filling_texts
                    filling_texts = "√"

                x = loc_list.loc[loc_list['坐标序列'] == filling_Number, '坐标X'].iloc[0]
                y = loc_list.loc[loc_list['坐标序列'] == filling_Number, '坐标Y'].iloc[0]

                text_position = (x, y)
                draw.text(text_position, filling_texts, font=font, fill=text_color)

            out_path = f'{destination_file_path}/temp/{page}.jpg'
            image.save(out_path)

        cls.combine_JPG2Pdf(destination_file_path, destination_file_path)


if __name__ == '__main__':
    # add remark
    KoreaVisa.fill_form('HID111-Test')
