import cv2
import pandas as pd
import os
from PIL import Image

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 500)

_path = 'E:/WORKING/C-Visa/MalaysiaVisa'


def show_image(name, form):
    cv2.namedWindow(name, 0)
    cv2.resizeWindow(name, 500, 740)

    cv2.imshow(name, form)
    cv2.waitKey(0)


def save_jpg():
    data = pd.read_excel(f'{_path}/VisaInform.xls', sheet_name='Sheet1')
    data = data[(data['Complete'] != 1) & (~data['fullname'].isnull())]

    for i in data.index:

        tel = str(data.loc[i, 'Tel'])
        eml = data.loc[i, 'Email']
        # print(tel)
        # exit()
        full_name = data.loc[i, 'fullname']

        gender = data.loc[i, 'gender']
        #
        # print(f"eml:{eml}")
        # print(f"tel:{tel}")

        s = 'X'

        birthPlace = data.loc[i, 'placebirth']

        birthDate = pd.to_datetime(data.loc[i, 'datebirth']).strftime('%d %b %Y')

        nationality = data.loc[i, 'nationality']
        occupation = data.loc[i, 'occupation']

        address = data.loc[i, 'addresS']
        address = address.split('/')

        marital = data.loc[i, 'marital']

        document = 'PASSPORT'
        numberPassport = data.loc[i, 'ppnumber']
        issuePlace = data.loc[i, 'ppissue']
        validDate = pd.to_datetime(data.loc[i, 'ppvalid']).strftime('%d %b %Y')

        formA = cv2.imread(f'{_path}/FormA.jpg')
        # formA = cv2.imread(f'FormA.jpg')

        # line 0  oversea
        cv2.putText(formA, s, (1538, 520), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2, cv2.LINE_AA)

        # line 1 full name
        cv2.putText(formA, full_name, (250, 910), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

        # line 2 sex
        if gender == 'M':
            sexLocation = (875, 1050)

        else:
            sexLocation = (1415, 1050)

        cv2.putText(formA, s, sexLocation, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2, cv2.LINE_AA)

        # tel
        cv2.putText(formA, tel, (1880, 1040), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

        # email
        cv2.putText(formA, eml, (1880, 1155), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

        # line3 place birth
        cv2.putText(formA, birthPlace, (680, 1165), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

        # line4 birth date
        cv2.putText(formA, birthDate, (680, 1300), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

        # line5 nationality
        cv2.putText(formA, nationality, (1580, 1290), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

        # line 6
        cv2.putText(formA, occupation, (680, 1490), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

        # line 7   line1
        cv2.putText(formA, address[0], (680, 1625), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

        # line 7   line2
        if len(address) >= 2:
            cv2.putText(formA, address[1], (680, 1700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

        # line 7   line3
        if len(address) >= 3:
            cv2.putText(formA, address[2], (680, 1780), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

        # line 8  single (410, 715), married (585, 715)
        if marital == 'S':  # single (410, 715), married (585, 715)
            maritalLocation = (1015, 1900)

        else:
            maritalLocation = (1450, 1900)

        cv2.putText(formA, s, maritalLocation, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2, cv2.LINE_AA)

        # line 11 travel document
        cv2.putText(formA, document, (800, 2250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

        # line 10
        cv2.putText(formA, numberPassport, (1950, 2245), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

        cv2.putText(formA, issuePlace, (800, 2410), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
        # line 12
        cv2.putText(formA, validDate, (1950, 2410), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
        # show_image('name', formA)
        # line 11
        cv2.imwrite(f'{_path}/out/HID{tel}_{full_name}_A.jpg', formA)
        # cv2.imwrite(f'out/HID{hid}_{full_name}_A.jpg', formA)

        # form B
        # addressM = data.loc[i, 'addressM']
        # addressM = addressM.split('/')

        formB = cv2.imread(f'{_path}/FormB.jpg')
        days = f'3 days'
        cv2.putText(formB, days, (1950, 1420), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

        # line 18 purposed
        cv2.putText(formB, s, (1400, 1625), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2, cv2.LINE_AA)

        # line sigal date
        date_ = pd.Timestamp('today').date().strftime('%d/%m/%Y')

        cv2.putText(formB, date_, (500, 2920), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2, cv2.LINE_AA)

        # show_image('name', formB)

        cv2.imwrite(f'{_path}/out/HID{tel}_{full_name}_B.jpg', formB)

        # cv2.imwrite(f'out/HID{hid}_{full_name}_B.jpg', formB)
        # exit()
        """ Form C information"""
        formC = cv2.imread(f'{_path}/FormC.jpg')
        # applicant name form C
        # print()
        cv2.putText(formC, full_name, (500, 3060), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(formC, numberPassport, (620, 3160), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(formC, date_, (450, 3240), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2, cv2.LINE_AA)

        author = 'ZHANG ZHUAN'
        cv2.putText(formC, author, (1550, 3060), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2, cv2.LINE_AA)
        author_id = 'S8865973B'
        cv2.putText(formC, author_id, (1800, 3160), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(formC, date_, (1550, 3240), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2, cv2.LINE_AA)

        cv2.imwrite(f'{_path}/out/HID{tel}_{full_name}_C.jpg', formC)

        """ Form D information"""
        formD = cv2.imread(f'{_path}/FormD.jpg')
        cv2.imwrite(f'{_path}/out/HID{tel}_{full_name}_D.jpg', formD)

        # show_image('name', formC)
        # exit()


def combine2Pdf():
    folderPath = f'{_path}/out/'
    pdfFilePath = f'{_path}/MalaysiaVsiaForm.pdf'
    files = os.listdir(folderPath)
    pngFiles = []
    sources = []

    for file in files:
        if 'jpg' in file:
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


def delete_jpg():
    images_files = os.listdir(f'{_path}/out/')

    for file in images_files:
        if file.endswith('.jpg'):
            os.remove(os.path.join(f'{_path}/out/', file))


if __name__ == '__main__':
    save_jpg()
    combine2Pdf()
    delete_jpg()
