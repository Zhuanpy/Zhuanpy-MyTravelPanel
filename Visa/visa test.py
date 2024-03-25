import cv2
import numpy as np
import csv

p = "E:\\WORKING\\A-AIR_TICKET\\01_Visa\\VisaDocumentRequirements\\01_Japan_visa\\Test"
# 读取大图和小图标
big_image = cv2.imread(f'{p}\\big_image.jpg')
small_icon = cv2.imread(f'{p}\\small_icon.png')

# 将小图标转换为灰度图像
small_gray = cv2.cvtColor(small_icon, cv2.COLOR_BGR2GRAY)

# 读取大图像并转换为灰度图像
big_image = cv2.cvtColor(big_image, cv2.COLOR_BGR2GRAY)

# 在大图中寻找小图标
result = cv2.matchTemplate(big_image, small_gray, cv2.TM_CCOEFF_NORMED)
threshold = 0.95  # 设定匹配阈值
locations = np.where(result >= threshold)

# 打开CSV文件以保存坐标
with open('coordinates.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['序号', 'X坐标', 'Y坐标'])

    # 循环遍历每个匹配的位置
    for i, loc in enumerate(zip(*locations[::-1])):

        x, y = loc
        print(x, y)
        # 在大图上绘制序号和坐标
        cv2.putText(big_image, str(i + 1), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.circle(big_image, (x, y), 5, (0, 255, 0), -1)
        # 将序号和坐标保存到CSV文件中
        csv_writer.writerow([i + 1, x, y])

# 保存标记后的大图
cv2.imwrite(f'{p}\\marked_image.jpg', big_image)
