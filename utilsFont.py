from PIL import Image, ImageDraw, ImageFont
import roman


def create_image(text, filename):
    # 创建一个白底图片
    width, height = 118, 118
    background_color = (210, 210, 210)  # 白色
    image = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(image)

    # 在图片上绘制数字1
    text_color = (0, 0, 0)  # 黑色
    font_size = 40
    font = ImageFont.truetype("Gabriola.ttf", font_size)  # 可以根据需要选择字体和字体大小
    text_width, text_height = draw.textsize(text, font)
    text_x = (width - text_width) / 2
    text_y = (height - text_height) / 2
    draw.text((text_x, text_y), text, fill=text_color, font=font)

    # 保存图片
    dpi = (300, 300)
    image.save(f"E:/WORKING/A-AIR_TICKET/math/{filename}.jpg", dpi=dpi)


def fulL_page(text: str, filename: str):
    # 创建一个白底图片
    width, height = 75, 75
    background_color = (255, 255, 255)  # 白色
    dpi = (300, 300)  # 分辨率为300dpi

    # for i in range(1, 11):
    # 创建一张新的图片
    image = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(image)

    # 在图片中央绘制数字
    # text = str(i)
    text_color = (0, 0, 0)  # 黑色

    # 计算字体大小以确保完全填充图片
    font_size = 1
    font = ImageFont.load_default()
    while font.getsize(text)[0] < width and font.getsize(text)[1] < height:
        font_size += 1
        font = ImageFont.truetype("Gabriola.ttf", font_size)

    text_width, text_height = draw.textsize(text, font)
    text_x = (width - text_width) / 2
    text_y = (height - text_height) / 2
    draw.text((text_x, text_y), text, fill=text_color, font=font)

    # 保存图片时设置分辨率
    image.save(f"E:/WORKING/A-AIR_TICKET/math/{filename}.jpg", dpi=dpi)


for i in range(1, 50):
    roman_numeral = roman.toRoman(i)
    text = f'{i}{roman_numeral}!'
    filename = str(i)
    fulL_page(text, filename)
