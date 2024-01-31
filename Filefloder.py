import os
import shutil

working_floder = 'E:/WORKING/A-AIR_TICKET'

working_visa_floder = os.path.join(working_floder, '01_Visa')

visa_requirements_floder = os.path.join(working_visa_floder, 'VisaDocumentRequirements')


def copy_folder_contents(source_folder, destination_folder):

    """ 将某个文件夹 A下所有内容， 复制到另外一个文件夹 B 下
    :parameter
    :source_folder: 文件夹 A 路径
    :destination_folder：文件夹 B 路径
    """

    # 确保目标文件夹存在， 不存在就创建文件夹；
    os.makedirs(destination_folder, exist_ok=True)

    # 遍历源文件夹中的所有文件
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)
        copy_file_path = os.path.join(destination_folder, filename)

        if os.path.isdir(source_path):
            # 如果是文件夹，递归调用函数
            copy_folder_contents(source_path, copy_file_path)

        else:
            # 如果是文件，使用shutil复制
            shutil.copy2(source_path, copy_file_path)
