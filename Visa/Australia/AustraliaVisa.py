import shutil
from Filefloder import *


def australia_visa_copy_all_files(name):

    source = os.path.join(visa_requirements_floder, '01_Australia_visa')

    name = f'Australia_VISA_{name}'

    destination_path = os.path.join(working_floder, name)

    # 确保目标文件夹存在
    os.makedirs(destination_path, exist_ok=True)

    # 遍历源文件夹中的所有文件
    for filename in os.listdir(source):
        source_path = os.path.join(source, filename)
        destination_path = os.path.join(destination_path, filename)

        # 使用 shutil.copy2 复制文件
        shutil.copy2(source_path, destination_path)


if __name__ == '__main__':
    # 示例用法
    destination_folder = 'liaovisa'
    australia_visa_copy_all_files(destination_folder)
