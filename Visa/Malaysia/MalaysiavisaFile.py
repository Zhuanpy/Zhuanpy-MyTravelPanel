from Filefloder import CreateVisaProgram as Program
import os


def malaysia_visa_copy_all_files(name):
    source_folder = os.path.join(Program.visa_requirements_folder, '01_Malaysia_visa')
    name = f'Malaysia_VISA_{name}'
    destination_folder = os.path.join(Program.working_visa_folder, name)
    Program.copy_folder_contents(source_folder, destination_folder)
    return True


if __name__ == '__main__':
    my_name = 'aaa'
    malaysia_visa_copy_all_files(my_name)
