import random
from PIL import Image, ImageDraw, ImageFont

# size: (1200, 712)
image = Image.open("./ID/id_base.png")
print(image.size, image.mode)

draw = ImageDraw.Draw(image)

font = ImageFont.truetype("./ID/標楷體.ttc", 100)
name = "鮭魚無敵好吃"
num = len(name)
spacing = 400 // (num - 1)
for i in range(num):
    draw.text((200 + i * spacing, 330), name[i], font = font, fill = "black")

font = ImageFont.truetype("./ID/標楷體.ttc", 50)
birthday = "100-01-01".split('-')
draw.text((300, 510), birthday[0], font = font, fill = "black")
draw.text((450, 510), birthday[1], font = font, fill = "black")
draw.text((590, 510), birthday[2], font = font, fill = "black")

draw.rectangle((0, 612, 750, 712), fill = "white")
font = ImageFont.truetype("./ID/標楷體.ttc", 50)
draw.text((30, 635), "娛樂用途，請勿當真或非法使用", font = font, fill = "red")

font = ImageFont.truetype("./ID/標楷體.ttc", 60)
draw.text((1040, 505), "男", font = font, fill = "black")

font = ImageFont.truetype("./ID/標楷體.ttc", 50)
city = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
city_number = {
    'A': 10,'B': 11,'C': 12,'D': 13,'E': 14,'F': 15,'G': 16,'H': 17,'I': 34,'J': 18,'K': 19,'L': 20,'M': 21,
    'N': 22,'O': 35,'P': 23,'Q': 24,'R': 25,'S': 26,'T': 27,'U': 28,'V': 29,'W': 32,'X': 30,'Y': 31,'Z': 33
}
id = f"{city}{1}"
number = city_number[city]
total = number / 10 + (number % 10) * 9 + 1 * 8
for i in range(7):
    temp = random.randint(0, 9)
    id += str(temp)
    total += temp * (7 - i)
draw.text((850, 635), f"{id}{10 - (int(total) % 10)}", font = font, fill = "black")

draw.rectangle((850, 80, 1150, 480), fill = "white")
icon = Image.open("./ID/avatar.png")
icon = icon.resize((300, 400))
image.paste(icon, (850, 80))

image.save("./ID/id_new.png")
