from Filefloder import CreateVisaProgram as Program
import os


class TaiwanVisa:

    @classmethod
    def taiwan_visa_copy_all_files(cls, name: str):
        """
        :param name: 输入签证的 HID号 + 名字
        :return:
        """
        # 项目资源文件夹
        source_folder = os.path.join(Program.visa_requirements_folder, '01_Taiwan_Visa')

        # 项目目标文件夹
        name = f'Taiwan_Visa_{name}'
        destination_folder = os.path.join(Program.working_folder, name)
        Program.copy_folder_contents(source_folder, destination_folder)

        return True


if __name__ == '__main__':
    file_name = "HID123_zhang zhuan"
    TaiwanVisa.taiwan_visa_copy_all_files(file_name)
