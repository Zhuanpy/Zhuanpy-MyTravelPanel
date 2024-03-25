from Filefloder import CreateVisaProgram as Program
import os


class MalaysiaVisa:

    @classmethod
    def create_visa_folder(cls, name):

        """
        :param name: 输入签证的 HID号 + 名字
        :return:
        """
        source_folder = os.path.join(Program.visa_requirements_folder, '01_Malaysia_visa')
        name = f'Malaysia_Visa_{name}'
        destination_folder = os.path.join(Program.working_visa_folder, name)
        Program.copy_folder_contents(source_folder, destination_folder)
        return True


if __name__ == '__main__':
    my_name = 'aaa'
    MalaysiaVisa.create_visa_folder(my_name)
