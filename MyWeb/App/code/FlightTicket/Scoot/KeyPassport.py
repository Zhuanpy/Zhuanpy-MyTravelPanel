import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

scoot_path = "E:/WORKING/A-AIR_TICKET/酷航/passport.xls"

pax_infor = pd.read_excel(scoot_path)
pax_infor = pax_infor[pax_infor["PAX"] != "案例"].reset_index(drop=True)
passport = pax_infor.loc[0, "PASSPORT"].split("/")
print(passport)
print(pax_infor)
title = passport[5]
first_name = passport[1]
last_name = passport[0]
date_of_birth = passport[4]
# birth_day = passport[5]
# birth_month = passport[5]
# birth_year = passport[5]
Nationality = passport[2]
passport_number = passport[3]

date_of_expiry = passport[6]
# expiry_day = passport[6]
# expiry_month = ""
# expiry_year = ""
residency = ""

# 获取坐标
# 点击
# 输入
# 判断是否需要下移点击

import cv2
import numpy as np


def find_icon_coordinates(big_image_path, small_icon_path, position_type=2, threshold=0.95):
    # 读取大图和小图标
    big_image = cv2.imread(big_image_path)
    small_icon = cv2.imread(small_icon_path)

    # 转换小图标为灰度图像
    small_gray = cv2.cvtColor(small_icon, cv2.COLOR_BGR2GRAY)

    # 读取大图像并转换为灰度图像
    big_gray = cv2.cvtColor(big_image, cv2.COLOR_BGR2GRAY)

    # 在大图中寻找小图标
    result = cv2.matchTemplate(big_gray, small_gray, cv2.TM_CCOEFF_NORMED)

    # 获取匹配结果大于阈值的位置
    locations = np.where(result >= threshold)

    # 提取匹配的坐标
    coordinates = []
    for pt in zip(*locations[::-1]):
        if position_type == 1:  # 最左边边中间点坐标
            x = pt[0]
            y = pt[1] + small_gray.shape[0] // 2
        elif position_type == 2:  # 中间点坐标
            x = pt[0] + small_gray.shape[1] // 2
            y = pt[1] + small_gray.shape[0] // 2
        elif position_type == 3:  # 最右边边中间点坐标
            x = pt[0] + small_gray.shape[1]
            y = pt[1] + small_gray.shape[0] // 2

        else:
            raise ValueError("position_type 参数必须是 1、2 或 3")

        coordinates.append((x, y))

    return coordinates


# 示例用法
big_image_path = 'big_image.jpg'
small_icon_path = 'small_icon.png'
position_type = 2
threshold = 0.8
icon_coordinates = find_icon_coordinates(big_image_path, small_icon_path, position_type, threshold)
print("匹配到的坐标：", icon_coordinates)
