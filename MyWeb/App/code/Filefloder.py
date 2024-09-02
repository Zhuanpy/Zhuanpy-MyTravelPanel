import os
import shutil


class CreateVisaFolder:
    base_path = r'E:\WORKING\A-AIR_TICKET'
    working_visa_folder = os.path.join(base_path, '01_Visa')
    visa_requirements_folder = os.path.join(working_visa_folder, 'VisaDocumentRequirements')

    @classmethod
    def copy_folder_contents(cls, source_folder: str, destination_folder: str, excluded_folders=None):
        """
        将某个文件夹 A 下所有内容复制到另外一个文件夹 B 下
        :parameter
        :source_folder: 文件夹 A 路径
        :destination_folder: 文件夹 B 路径
        :excluded_folders: 不需要复制的文件夹列表
        """

        if excluded_folders is None:
            excluded_folders = []

        # 确保目标文件夹存在，不存在就创建文件夹
        os.makedirs(destination_folder, exist_ok=True)

        # 遍历源文件夹中的所有文件
        for filename in os.listdir(source_folder):
            source_path = os.path.join(source_folder, filename)
            copy_file_path = os.path.join(destination_folder, filename)

            # 检查是否需要排除该文件夹
            if os.path.isdir(source_path):
                if filename not in excluded_folders:
                    # 如果是文件夹，递归调用函数
                    cls.copy_folder_contents(source_path, copy_file_path, excluded_folders)
            else:
                # 如果是文件，使用shutil复制
                shutil.copy2(source_path, copy_file_path)

        return True

    @classmethod
    def create_folder(cls, country: str, name: str, excluded_folders=None):
        """
        创建签证文件夹并复制文件内容
        :param country: 签证国家
        :param name: 输入签证的 HID号 + 名字
        :excluded_folders: 不需要复制的文件夹列表
        :return: True
        """

        if excluded_folders is None:
            excluded_folders = []

        # 项目资源文件夹
        source_folder = os.path.join(cls.visa_requirements_folder, f'01_{country}_Visa')

        # 项目目标文件夹
        destination_folder_name = f'{country}_Visa_{name}'
        destination_folder = os.path.join(cls.base_path, destination_folder_name)

        # 复制文件夹内容
        cls.copy_folder_contents(source_folder, destination_folder, excluded_folders)

        return True

    @classmethod
    def Taiwan_folder(cls, name: str):
        """
        创建台湾签证文件夹并复制文件内容
        :param name: 输入签证的 HID号 + 名字
        :return: True
        """
        return cls.create_folder('Taiwan', name)

    @classmethod
    def Us_folder(cls, name: str):
        """
        创建美国签证文件夹并复制文件内容
        :param name: 输入签证的 HID号 + 名字
        :return: True
        """
        return cls.create_folder('Us', name)

    @classmethod
    def NewZealand_folder(cls, name: str):
        return cls.create_folder('NewZealand', name)

    @classmethod
    def Australia_folder(cls, name: str):
        return cls.create_folder('Australia', name)

    @classmethod
    def Malaysia_folder(cls, name: str):
        return cls.create_folder('Malaysia', name)

    @classmethod
    def Uk_folder(cls, name: str):
        return cls.create_folder('Uk', name)

    @classmethod
    def Korea_folder(cls, name: str):
        excluded_folders = ["KoraVisaForm", "source"]
        return cls.create_folder('Korea', name, excluded_folders)

    @classmethod
    def Japan_folder(cls, name: str):
        return cls.create_folder('Japan', name)

    @classmethod
    def China_folder(cls, name: str):
        return cls.create_folder('China', name)

    @classmethod
    def ChinaPassport_folder(cls, name: str):
        return cls.create_folder('ChinaPassport', name)

    @classmethod
    def Schengen_folder(cls, name: str):
        return cls.create_folder('Schengen', name)
