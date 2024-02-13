from pathlib import Path
import pandas as pd
import shutil
from PIL import Image, ImageDraw, ImageFont
import os

root_path = "E:/WORKING/A-AIR_TICKET"
data_path = f"{root_path}/01_Visa/VisaDocumentRequirements/01_Korea_vsia"


def combine_JPG2Pdf(folderPath: str, pdfFilePath: str):

    folderPath = f'{folderPath}temp/'

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


def create_korea_visa_folder(file_name: str):

    try:
        file_name = file_name.upper()
        folder_name = f'KOR_VISA_{file_name}'

        folder_path = Path(f'{root_path}/{folder_name}')
        folder_path.mkdir(parents=True)

        # 创建子文件夹
        temp = Path(f'{root_path}/{folder_name}/temp')
        temp.mkdir(parents=True)

        """ 复制 文档列表 excel """
        document_list_source_path = f'{data_path}/DocumentList.xls'
        document_list_destination_path = f'{folder_path}/DocumentList.xls'
        shutil.copy(document_list_source_path, document_list_destination_path)

        """ 复制 表格 excel """
        form_source_path = f'{data_path}/FormSample.xls'
        form_destination_path = f'{folder_path}/FormSample.xls'
        shutil.copy(form_source_path, form_destination_path)

    except FileExistsError:
        pass


def fill_korea_visa_form(folder: str):
    folder = f'KOR_VISA_{folder}'
    file_path = f'{root_path}/{folder}'

    for p in range(1, 6):
        page = f'PAGE0{p}'

        """ 读取坐标信息 """
        loc_list = pd.read_excel(f'{data_path}/图片坐标列表.xls', sheet_name='Sheet1')
        loc_list = loc_list[loc_list['页面'] == page]

        """  清理填写表格信息 """
        form = pd.read_excel(f'{file_path}/FormSample.xls', sheet_name='Sheet1')
        form = form[form['PAGE'] == page]
        form = form[~(form['序列'].isnull())]
        form['序列'] = form['序列'].astype(int)
        form = form[(form['序列'] > 0) & (form['DETAIL'] != 'N/A')]
        form = form[~(form['DETAIL'].isnull())]
        loc_list['图片名'] = loc_list['图片名'].astype(int)

        image_path = f'{data_path}/Form-page-{p}.jpg'
        image = Image.open(image_path)
        # 创建一个Draw对象
        draw = ImageDraw.Draw(image)
        # 选择字体,字号,颜色
        font = ImageFont.truetype("simsun.ttc", 50)  # 楷体字体文件
        text_color = (48, 97, 174)  # # 选择文字颜色

        for i in form.index:
            texts = str(form.loc[i, 'DETAIL'])
            temp_name = form.loc[i, '序列']
            temp_loc = loc_list[loc_list['图片名'] == temp_name]['坐标'].iloc[0]

            # print(temp_loc)
            temp_loc = temp_loc[1:-1].split(',')
            x = int(temp_loc[0])
            y = int(temp_loc[1])
            text_position = (x, y)
            draw.text(text_position, texts, font=font, fill=text_color)

        out_path = f'{root_path}/{folder}/temp/{page}.jpg'
        image.save(out_path)

    folderPath = f'{file_path}/'
    pdfFilePath = f'{file_path}'
    combine_JPG2Pdf(folderPath, pdfFilePath)


if __name__ == '__main__':
    # add remark
    fill_korea_visa_form('KOR_VISA_HID153215-HANHAN')
