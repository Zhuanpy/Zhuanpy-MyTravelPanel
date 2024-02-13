from Filefloder import CreateVisaProgram as Program
import os


def australia_visa_copy_all_files(name):
    name = f'Australia_VISA_{name}'
    source_folder = os.path.join(Program.visa_requirements_folder, '01_Australia_visa')
    destination_folder = os.path.join(Program.working_folder, name)
    Program.copy_folder_contents(source_folder, destination_folder)
    return True


if __name__ == '__main__':
    destination = 'liaovisa'
    australia_visa_copy_all_files(destination)
