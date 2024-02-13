import os
from PyPDF2 import PdfMerger
from PIL import Image


class MyPdfFile:

    def __init__(self, folder: str):
        self.files = folder

    def merge_pdf2pdf(self):

        output_path = os.path.join(self.files, 'MyPdf.pdf')

        pdf_lst = [f for f in os.listdir(self.files) if f.endswith('.pdf')]

        pdf_lst = [os.path.join(self.files, filename) for filename in pdf_lst]

        file_merger = PdfMerger()

        for f in pdf_lst:
            file_merger.append(f)  # 合并pdf文件

        file_merger.write(output_path)

    # Merge images into PDF
    def merge_images2pdf(self):
        pdfFilePath = os.path.join(self.files, 'CombinePdf.pdf')
        files = os.listdir(self.files)

        files_list = []
        sources = []

        image_extensions = ['jpg', 'png', 'jpeg', 'webp']

        for file in files:
            split_files = file.split('.')
            extension = split_files[-1].lower()

            if extension in image_extensions:
                file_path_ = os.path.join(self.files, file)
                try:
                    if int(split_files[0]) <= 5 and len(split_files[0]) == 1:
                        continue
                    files_list.append(file_path_)

                except ValueError:
                    files_list.append(file_path_)

        files_list.sort()
        output = Image.open(files_list[0])
        files_list.pop(0)

        for file in files_list:

            pngFile = Image.open(file)

            if pngFile.mode == "RGB":
                pngFile = pngFile.convert("RGB")

            sources.append(pngFile)

        output.save(pdfFilePath, "pdf", save_all=True, append_images=sources)


if __name__ == "__main__":

    file_path = """ E:\WORKING\A-AIR_TICKET\HID159187_GAO YICHEN\Datebirth """

    pdf = MyPdfFile(file_path)
    pdf.merge_images2pdf()
