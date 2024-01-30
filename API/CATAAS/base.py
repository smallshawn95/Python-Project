# CATAAS API
# URL: https://cataas.com/

import io
import requests
from PIL import Image

png_url = "https://cataas.com/cat"
png = requests.get(png_url)

# 直接預覽圖片
# Image.open(io.BytesIO(png.content)).show()

with open("./API/CATAAS/cat.png", "wb") as file:
    file.write(png.content)

gif_url = "https://cataas.com/cat/gif"
gif = requests.get(gif_url)

with open("./API/CATAAS/cat.gif", "wb") as file:
    file.write(gif.content)

text = "Hello, world!"
says_url = f"https://cataas.com/cat/says/{text}"
says = requests.get(says_url)

with open("./API/CATAAS/cat_say.png", "wb") as file:
    file.write(says.content)
