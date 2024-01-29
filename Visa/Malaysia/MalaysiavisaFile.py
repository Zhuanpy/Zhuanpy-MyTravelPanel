from Filefloder import *


def malaysia_visa_copy_all_files(name):
    source_folder = os.path.join(visa_requirements_floder, '01_Malaysia_visa')
    name = f'Malaysia_VISA_{name}'
    destination_folder = os.path.join(working_floder, name)
    copy_folder_contents(source_folder, destination_folder)
    return True


if __name__ == '__main__':
    my_name = 'aaa'
    malaysia_visa_copy_all_files(my_name)
