from flask import Blueprint, render_template, request
from Visa.VisaPdfFile.pdffile import MyPdfFile

# 创建蓝图
fpb = Blueprint('files_routes', __name__)


@fpb.route('/pdf_to_pdf', methods=['GET', 'POST'])
def merge_pdf_to_pdf():
    if request.method == 'POST':
        # 获取输入的文件夹路径
        folder_path = request.form['folder_path']
        # 处理图片并生成PDF
        my_pdf = MyPdfFile(folder_path)
        my_pdf.merge_images2pdf()
        my_pdf.merge_pdf2pdf()

        # 返回结果页面
        return render_template('result.html', folder_path=folder_path)

    # 如果是 GET 请求，返回包含输入框的表单页面

    return render_template('file_processing.html')


@fpb.route('/images_to_pdf', methods=['POST'])
def merge_images_to_pdf():
    # 获取输入的文件夹路径
    folder_path = request.form.get['imageFolderPath']
    # file_path = request.form.get("path_create_project")
    print(folder_path)
    # 处理图片并生成PDF
    # my_pdf = MyPdfFile(folder_path)
    # my_pdf.merge_images2pdf()

    # 返回结果页面
    return render_template('result.html', folder_path=folder_path)

