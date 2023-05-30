from pygments import lexers
from pygments import highlight
from pygments.styles import get_style_by_name
from pygments.formatters.html import HtmlFormatter

code = "print('Hello World!')"
lexer = lexers.get_lexer_by_name("python")
style = get_style_by_name("native")
formatter = HtmlFormatter(full = True, style = style)

with open("screenshot.html", "w", encoding = "utf8") as file:
    highlight(code, lexer, formatter, outfile = file)