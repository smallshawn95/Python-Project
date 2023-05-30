from pygments import lexers
from pygments import highlight
from pygments.styles import get_style_by_name
from pygments.formatters.img import ImageFormatter

code = "print('Hello World!')\nprint('Hello Python!')"
lexer = lexers.get_lexer_by_name("python")
style = get_style_by_name("native")

# line_pad(2) 間距像素
# font_name(Courier New) 字體名稱
# font_size(14) 字體大小
# image_pad(10) 圖片邊距像素
# line_numbers(True) 行號顯示
# line_number_start(1) 第一行行號
# line_number_step(1) 行號間隔
# line_number_bg(#eed) 行號背景顏色
# line_number_fg(#886) 行號文字顏色
# line_number_chars(2) 行號邊距列數
# line_number_bold(False) 行號加粗
# line_number_italic(False) 行號斜體
# line_number_separator(True) 行號和程式碼之間劃線
# line_number_pad(6) 行號和程式碼間距像素
# hl_lines(empty list) 凸顯行數列表
# hl_color 凸顯顏色
formatter = ImageFormatter(
    line_pad = 5,
    font_name = "JetBrains Mono",
    font_size = 16,
    line_number_bold = True,
    line_number_pad = 15,
    full = True,
    style = style
)

with open("screenshot.png", "wb") as file:
    file.write(highlight(code, lexer, formatter))
