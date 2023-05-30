from pygments import lexers
from pygments import highlight
from pygments.styles import get_style_by_name
from pygments.formatters.img import ImageFormatter

code = "print('Hello World!')"
lexer = lexers.get_lexer_by_name("python")
style = get_style_by_name("native")
formatter = ImageFormatter(full = True, style = style)

with open("screenshot.png", "wb") as file:
    file.write(highlight(code, lexer, formatter))