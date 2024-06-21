from Filefloder import CreateVisaProgram as Program
import os


class AustraliaVisa:

    @classmethod
    def create_visa_folder(cls, name: str):
        """
        :param name: 输入签证的 HID号 + 名字
        :return:
        """
        # 项目资源文件夹
        source_folder = os.path.join(Program.visa_requirements_folder, '01_Australia_visa')
        print(source_folder)

        # 项目目标文件夹
        name = f'Australia_Visa_{name}'
        destination_folder = os.path.join(Program.working_folder, name)
        print(destination_folder)

        Program.copy_folder_contents(source_folder, destination_folder)

        return True


if __name__ == '__main__':
    destination = 'liaovisa'

