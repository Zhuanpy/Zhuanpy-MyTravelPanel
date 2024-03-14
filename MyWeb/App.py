from flask import Flask, render_template, request
from Visa.VisaPdfFile.pdffile import MyPdfFile

from routes_visa import bp as visa_routes

app = Flask(__name__)

app.register_blueprint(visa_routes)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/visa')
def visa():
    return render_template('visa.html')


@app.route('/flight')
def flight():
    return render_template('flight.html')


@app.route('/accommodation')
def accommodation():
    return render_template('package.html')


@app.route('/file_processing', methods=['GET', 'POST'])
def file_processing():
    if request.method == 'POST':
        # 获取输入的文件夹路径
        folder_path = request.form['folder_path']
        print(folder_path)
        # 处理图片并生成PDF
        my_pdf = MyPdfFile(folder_path)
        my_pdf.merge_images2pdf()

        # 返回结果页面
        return render_template('result.html', folder_path=folder_path)

    # 如果是 GET 请求，返回包含输入框的表单页面

    return render_template('file_processing.html')


@app.route('/my_test')
def my_test():
    return render_template("Test.html")


# @app.route('/KoreaVisaProject')
# def create_korea_visa_project(file_name):
#     create_korea_visa_folder(file_name)
#     return ""


if __name__ == '__main__':
    app.run(debug=True)
