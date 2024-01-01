from pathlib import Path


def create_my_folder(file_type: str, hid: str, name: str, file_path=None):

    _path = "E:/WORKING/A-AIR_TICKET"

    if file_path:
        _path = f'{_path}/{file_path}'

    file_type = file_type.upper()
    name = name.upper()
    folder = f'{file_type}_VISA_HID{hid}_{name}'

    path = Path(f'{_path}/{folder}')

    path.mkdir(parents=True)


if __name__ == '__main__':
    a, b, c = 'China', '123', 'Huang li'
    create_my_folder(a, b, c)
