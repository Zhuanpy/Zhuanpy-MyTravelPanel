from Filefloder import *


def australia_visa_copy_all_files(name):
    name = f'Australia_VISA_{name}'
    source_folder = os.path.join(visa_requirements_floder, '01_Australia_visa')
    destination_folder = os.path.join(working_floder, name)
    copy_folder_contents(source_folder, destination_folder)
    return True


if __name__ == '__main__':
    destination = 'liaovisa'
    australia_visa_copy_all_files(destination)
