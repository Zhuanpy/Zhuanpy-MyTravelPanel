from flask import Blueprint, render_template, request
from Visa.VisaPdfFile.pdffile import MyPdfFile

# 创建蓝图
fpb = Blueprint('files_routes', __name__)


@fpb.route('/pdf_to_pdf', methods=['POST'])
def merge_pdf_to_pdf():
    path = request.form.get('pdfFolderPath')
    # 处理图片并生成PDF
    f = MyPdfFile(path)
    f.merge_pdf2pdf()
    return render_template('result.html')


@fpb.route('/images_to_pdf', methods=['POST'])
def merge_images_to_pdf():
    # 获取输入的文件夹路径
    path = request.form.get('imageFolderPath')
    # 处理图片并生成PDF
    f = MyPdfFile(path)
    f.merge_images2pdf()
    # 返回结果页面
    return render_template('result.html', folder_path=path)

