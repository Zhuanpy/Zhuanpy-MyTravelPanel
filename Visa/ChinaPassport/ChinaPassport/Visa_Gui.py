import cv2
from PIL import Image, ImageDraw, ImageFont


def get_locations(large_image, small_image):  # 获取图片坐标函数

    # 读取大图片和小图片
    large_image = cv2.imread(large_image)
    small_image = cv2.imread(small_image)

    # 使用匹配方法
    result = cv2.matchTemplate(large_image, small_image, cv2.TM_CCOEFF_NORMED)

    # 获取最大匹配位置
    _, _, _, max_loc = cv2.minMaxLoc(result)

    # 获取小图标位置
    x, y = max_loc

    # 打印小图标在大图片中的位置

    return x, y


# 定义获取输入内容的函数
def get_input(text_name, text_order_num):
    # 添加文字到图片
    print("名字:", text_name)
    print("订单号:", text_order_num)

    l_tf = 'TargetForm.jpg'
    l_name = 'TargetName.jpg'
    l_num = 'TargetBookingNo.jpg'

    x1, y1 = get_locations(l_tf, l_name)
    x2, y2 = get_locations(l_tf, l_num)

    print("小图标在大图片中的位置：({}, {})".format(x1, y1))
    print("小图标在大图片中的位置：({}, {})".format(x2, y2))

    # exit()
    # 打开图片
    image = Image.open('FillForm.jpg')

    # 创建一个Draw对象
    draw = ImageDraw.Draw(image)

    # 选择字体和字号
    font = ImageFont.truetype("simsun.ttc", 50)  # 楷体字体文件

    # 选择文字颜色
    text_color = (0, 0, 0)  # 白色

    # 添加 customer name 到图片
    text_position = (x1, y1)  # 文字在图片中的位置，以左上角为原点
    draw.text(text_position, text_name, font=font, fill=text_color)  #

    # 添加 order num 到图片
    text_position = (x2, y2)
    draw.text(text_position, text_order_num, font=font, fill=text_color)  #

    # 保存修改后的图片
    image.save(f'E:/WORKING/A-AIR_TICKET/{text_name}_到馆登记表.jpg')
