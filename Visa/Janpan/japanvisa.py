from Filefloder import CreateVisaProgram as Program
import os


def create_japan_visa_folder(name: str):

    """
    :param name: 输入签证的 HID号 + 名字
    :return:
    """
    source_folder = os.path.join(Program.visa_requirements_folder, '01_Japan_visa')
    name = f'Japan_Visa_{name}'
    destination_folder = os.path.join(Program.working_folder, name)
    Program.copy_folder_contents(source_folder, destination_folder)

    return True


if __name__ == '__main__':
    # 示例用法
    folder = 'liaovisa'
    create_japan_visa_folder(folder)
