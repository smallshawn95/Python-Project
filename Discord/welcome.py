import cv2, numpy, random
from PIL import Image, ImageDraw, ImageFont

def circle_image(image, height, width):
    image = cv2.resize(image, (height, width))
    circle = numpy.zeros((height, width, 1), numpy.uint8)
    # 圓形設定：Image, 中心點座標, 半徑, (B, G, R), Thickness
    circle = cv2.circle(circle, (width // 2, height // 2), min(height, width) // 2, (1), -1)
    new_image = numpy.zeros((height, width, 4), numpy.uint8)
    new_image[:, :, 0] = numpy.multiply(image[:, :, 0], circle[:, :, 0])
    new_image[:, :, 1] = numpy.multiply(image[:, :, 1], circle[:, :, 0])
    new_image[:, :, 2] = numpy.multiply(image[:, :, 2], circle[:, :, 0])
    circle[circle == 1] = 255
    new_image[:, :, 3] = circle[:, :, 0]
    return new_image

def black_background(image, height, width):
    image = cv2.resize(image, (height, width))
    for i in range(height):
        for j in range(width):
            if sum(image[i][j]) == 0:
                image[i][j] = numpy.array([0, 0, 0, 0])
    return image

# cv2 加入中文字
def cv2Image_add_chineseText(image, text, left, top, textColor = (255, 255, 255), textSize = 100):
    image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image)
    fontText = ImageFont.truetype("./Discord/GenYoGothic-M.ttc", textSize)
    draw.text((left, top), text, textColor, font = fontText)
    return cv2.cvtColor(numpy.asarray(image), cv2.COLOR_RGB2BGR)

def average_color(image):
    size = image.size // 3
    temp = cv2.split(image)
    blues, greens, reds = temp[0], temp[1], temp[2]
    b, g, r = 0, 0, 0
    for blue in blues:
        b += sum(blue)
    for green in greens:
        g += sum(green)
    for red in reds:
        r += sum(red)
    b, g, r = b // size, g // size, r // size
    if b < 100:
        b = random.randint(100, 200)
    if g < 100:
        g = random.randint(100, 200)
    if r < 100:
        r = random.randint(100, 200)
    return (int(b), int(g), int(r))

image = numpy.zeros((720, 1280, 4), numpy.uint8)
icon = cv2.imread("./Discord/avatar.png", cv2.IMREAD_UNCHANGED)
icon_color = average_color(icon)
new_icon = circle_image(icon, 500, 500)
guild = cv2.imread("./Discord/guild.png", cv2.IMREAD_UNCHANGED)
guild_color = average_color(guild)
guild = black_background(guild, 200, 200)
new_guild = circle_image(guild, 200, 200)
image[110:610, 50:550] = new_icon
image[480:680, 1020:1220] = new_guild
# print(icon_color, guild_color)
temp = "HelloWorld#123".split('#')
name = temp[0]
number = f"#{temp[1]}"
if len(name) > 10:
    fontSize, add = 70, 0
elif len(name) < 5:
    fontSize, add = 90, 20
else:
    fontSize, add = 80, 10
image = cv2Image_add_chineseText(image, name, 620, 350, (icon_color[2], icon_color[1], icon_color[0]), fontSize)
image = cv2Image_add_chineseText(image, number, 620, 450 + add, (icon_color[2], icon_color[1], icon_color[0]), fontSize)
# 文字設定：Image, Text, (x, y), FontFace, FontScale, (B, G, R), Thickness, LineType
cv2.putText(image, "Hello, world!", (620, 250), cv2.FONT_HERSHEY_SIMPLEX, 3, (guild_color[0], guild_color[1], guild_color[2]), 10, cv2.LINE_AA)
cv2.imwrite("./Discord/welcome.png", image)
