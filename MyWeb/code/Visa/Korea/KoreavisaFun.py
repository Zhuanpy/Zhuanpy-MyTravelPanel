import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os


class KoreaVisa:

    @classmethod
    def combine_JPG2Pdf(cls, folderPath: str, pdfFilePath: str):
        """
        将指定文件夹中的图片合并为 PDF 文件。

        :param folderPath: 包含图片的文件夹路径
        :param pdfFilePath: 生成的 PDF 文件路径

        """

        # 设定输出 PDF 文件路径
        pdfFilePath = os.path.join(pdfFilePath, 'my_visa_form.pdf')

        # 获取文件夹中的所有文件
        files = os.listdir(folderPath)
        pngFiles = []
        sources = []

        THRESHOLD_VALUE = 0  # 设定不转化的图片的阈值
        for file in files:
            # 筛选出图片文件
            if any(ext in file.lower() for ext in ['jpg', 'png', 'jpeg', 'webp']):
                filename = os.path.splitext(file)[0]

                try:
                    # 判断文件名是否为大于阈值的数字
                    if int(filename) > THRESHOLD_VALUE:
                        pngFiles.append(os.path.join(folderPath, file))

                except ValueError:
                    # 如果文件名不是数字，直接添加
                    pngFiles.append(os.path.join(folderPath, file))

        pngFiles.sort()
        output = Image.open(pngFiles[0])
        pngFiles.pop(0)

        for file in pngFiles:

            pngFile = Image.open(file)
            # 确保图片模式为 RGB
            if pngFile.mode == "RGB":
                pngFile = pngFile.convert("RGB")

            sources.append(pngFile)

        # 保存为 PDF 文件
        output.save(pdfFilePath, "pdf", save_all=True, append_images=sources)

    @classmethod
    def fill_form(cls, folder: str):
        """
        根据提供的表格信息填充表单，并生成对应的图片和 PDF 文件。

        :param folder: 目标文件夹名称

        """
        folder_title = "Korea_Visa"
        base_path = r'E:\WORKING\A-AIR_TICKET'

        form_folder = f'{folder_title}_{folder}'
        form_path = os.path.join(base_path, form_folder)
        form_temp_path = os.path.join(form_path, "temp")

        source_path = os.path.join(base_path, "01_Visa", "VisaDocumentRequirements", "01_Korea_visa", "source")

        for p in range(1, 6):

            page = f'PAGE0{p}'
            loc_file = os.path.join(source_path, "坐标列表.xls")
            # 读取坐标信息
            loc_list = pd.read_excel(loc_file, sheet_name='Sheet1')
            loc_list = loc_list[loc_list['PAGE'] == page]
            loc_list[["坐标序列"]] = loc_list[["坐标序列"]].astype(str)
            loc_list[["坐标X", "坐标Y"]] = loc_list[["坐标X", "坐标Y"]].astype(int)

            # 清理填写表格信息
            form_sample = os.path.join(form_path, "FormSample.xls")
            form = pd.read_excel(form_sample, sheet_name='Sheet1')
            form = form[form['PAGE'] == page]
            form = form[~(form['DETAIL'].isnull())]
            form[["坐标序列", "DETAIL"]] = form[["坐标序列", "DETAIL"]].astype(str)

            # 打开图片并创建绘图对象
            image_name = f"Form-page-{p}.jpg"
            image_path = os.path.join(source_path, image_name)
            image = Image.open(image_path)
            draw = ImageDraw.Draw(image)

            # 设置字体、字号和颜色
            font = ImageFont.truetype("simsun.ttc", 50)  # 楷体字体文件
            text_color = (0, 0, 255)  # 文字颜色

            for i in form.index:
                filling_texts = form.loc[i, 'DETAIL']
                form_type = form.loc[i, '类型']
                filling_Number = form.loc[i, '坐标序列']

                if form_type == "选择":
                    filling_Number = filling_Number + filling_texts
                    filling_texts = "√"

                x = loc_list.loc[loc_list['坐标序列'] == filling_Number, '坐标X'].iloc[0]
                y = loc_list.loc[loc_list['坐标序列'] == filling_Number, '坐标Y'].iloc[0]

                text_position = (x, y)
                draw.text(text_position, filling_texts, font=font, fill=text_color)

            image_name = f"{page}.jpg"
            image.save(f"{form_temp_path}/{image_name}")

        cls.combine_JPG2Pdf(form_temp_path, form_path)


if __name__ == '__main__':
    # add remark
    KoreaVisa.fill_form('HID111-Test')
