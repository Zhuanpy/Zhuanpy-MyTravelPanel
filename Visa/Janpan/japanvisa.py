import shutil
import os


def japan_visa_copy_all_files(name):
    source = 'E:/WORKING/A-AIR_TICKET/01_Visa/VisaDocumentRequirements/01_Japan_visa'
    destination = 'E:/WORKING/A-AIR_TICKET'
    name = f'JAN_VISA_{name}'
    destination = os.path.join(destination, name)

    # 确保目标文件夹存在
    os.makedirs(destination, exist_ok=True)

    # 遍历源文件夹中的所有文件
    for filename in os.listdir(source):
        source_path = os.path.join(source, filename)
        destination_path = os.path.join(destination, filename)

        # 使用 shutil.copy2 复制文件
        shutil.copy2(source_path, destination_path)


if __name__ == '__main__':
    # 示例用法
    destination_folder = 'liaovisa'
    japan_visa_copy_all_files(destination_folder)
