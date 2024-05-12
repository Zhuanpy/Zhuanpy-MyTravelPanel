from pathlib import Path
import os
from Filefloder import CreateVisaProgram as Program


def create_my_folder(file_type: str, hid: str, name: str, file_path=None):
    if file_path:
        _path = os.path.join(Program.working_folder, file_path)

    file_type = file_type.upper()
    name = name.upper()
    folder = f'{file_type}_VISA_HID{hid}_{name}'

    path = Path(f'{Program.working_folder}/{folder}')

    path.mkdir(parents=True)


if __name__ == '__main__':
    # self._path = 'E:/WORKING/B-账单/BOOKING'
    # _path = os.path.join("E:",   "WORKING", "B-账单", "BOOKING")
    # print(_path)
    # exit()
    # a, b, c = 'China', '123', 'Huang li'
    # create_my_folder(a, b, c)
    print("MY TEST")
