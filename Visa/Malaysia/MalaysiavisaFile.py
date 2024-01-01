import os
from PyPDF2 import PdfMerger
from PIL import Image


class MalaysiaVisa:

    def __init__(self, folder: str):
        self.files = folder

    def merge_pdf(self):

        input_path = f'E:/WORKING/A-AIR_TICKET/{self.files}/'
        output_path = f'E:/WORKING/A-AIR_TICKET/{self.files}/myic.pdf'

        pdf_lst = [f for f in os.listdir(input_path) if f.endswith('.pdf')]

        pdf_lst = [os.path.join(input_path, filename) for filename in pdf_lst]

        file_merger = PdfMerger()
        for pdf in pdf_lst:
            file_merger.append(pdf)  # 合并pdf文件

        file_merger.write(output_path)

    def combine2Pdf(self):

        folderPath = f'E:/WORKING/A-AIR_TICKET/{self.files}/'
        pdfFilePath = f'E:/WORKING/A-AIR_TICKET/{self.files}/combinetomyic.pdf'

        files = os.listdir(folderPath)
        pngFiles = []
        sources = []
        for file in files:

            if 'jpg' in file:

                filename = file.split('.')[0]

                try:
                    if int(filename) > 5:
                        pngFiles.append(folderPath + file)
                except:

                    pngFiles.append(folderPath + file)

            if 'png' in file:

                filename = file.split('.')[0]

                try:
                    if int(filename) > 5:
                        pngFiles.append(folderPath + file)
                except:

                    pngFiles.append(folderPath + file)

            if 'jpeg' in file:

                filename = file.split('.')[0]

                try:
                    if int(filename) > 5:
                        pngFiles.append(folderPath + file)
                except:

                    pngFiles.append(folderPath + file)

            if 'webp' in file:

                filename = file.split('.')[0]

                try:
                    if int(filename) > 5:
                        pngFiles.append(folderPath + file)
                except:

                    pngFiles.append(folderPath + file)

        pngFiles.sort()
        output = Image.open(pngFiles[0])
        pngFiles.pop(0)

        for file in pngFiles:

            pngFile = Image.open(file)

            if pngFile.mode == "RGB":
                pngFile = pngFile.convert("RGB")

            sources.append(pngFile)

        output.save(pdfFilePath, "pdf", save_all=True, append_images=sources)

    # def pdf2jpg(self, input_path, output_path):
    #
    #     pdf_document = fitz.open(pdf_path)
    #
    #     # 逐页将PDF转换为JPG图像
    #     for page_number in range(pdf_document.page_count):
    #         page = pdf_document.load_page(page_number)
    #         pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # 调整图像大小
    #
    #         image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    #         image_path = f"{output_folder}/page_{page_number + 1}.jpg"
    #         image.save(image_path)
    #         print(f"Page {page_number + 1} converted and saved as {image_path}")
    #
    #     # 关闭PDF文件
    #     pdf_document.close()



