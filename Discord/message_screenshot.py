from PIL import Image, ImageDraw, ImageFont

image = Image.new("RGB", (800, 60), "#313338")
draw = ImageDraw.Draw(image)
avatar = Image.open("./Discord/avatar.png").resize((40, 40))
mask = Image.new("RGBA", (400, 400), color = (0, 0, 0, 0))
mask_draw = ImageDraw.Draw(mask)
mask_draw.ellipse((0, 0, 400, 400), fill = (0, 0, 0, 255))
image.paste(
    im = avatar,
    box = (10, 10),
    mask = mask.resize((40, 40))
)
font = ImageFont.truetype("./Discord/msjhbd.ttc", 14)
draw.text((65, 10), "燒雞版主 — SmallShawn95", "#87cefa", font = font)
length = font.getlength("燒雞版主 — SmallShawn95")
font = ImageFont.truetype("./Discord/msjhbd.ttc", 12)
draw.text((75 + length, 12), "2023/07/27 16:20", "#949ba4", font = font)
font = ImageFont.truetype("./Discord/msjhbd.ttc", 14)
draw.text((65, 32), "沒錢錢 :bee~1:", "#ffffff", font = font)
image.save("./Discord/image.png")
