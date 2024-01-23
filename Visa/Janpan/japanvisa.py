from Filefloder import *


def japan_visa_copy_all_files(name):
    source_folder = os.path.join(visa_requirements_floder, '01_Japan_visa')
    name = f'JAN_VISA_{name}'
    destination_folder = os.path.join(working_floder, name)
    copy_folder_contents(source_folder, destination_folder)
    return True


if __name__ == '__main__':
    # 示例用法
    folder = 'liaovisa'
    japan_visa_copy_all_files(folder)
