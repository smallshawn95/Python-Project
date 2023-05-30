import json
from pygments import lexers
from pygments import highlight
from pygments.styles import get_style_by_name
from pygments.formatters.img import ImageFormatter

code = '''
#include <iostream>
using namespace std;

int main()
{
    cout << "Hello, world!" << endl;
    return 0;
}
'''
lexer = lexers.get_lexer_by_name("cpp")

with open("pygments.json", "r", encoding = "utf8") as file:
    data = json.load(file)

for style in data["styles"]:
    formatter = ImageFormatter(
        line_pad = 5,
        font_name = "JetBrains Mono",
        font_size = 16,
        line_number_bold = True,
        line_number_pad = 15,
        style = get_style_by_name(style)
    )
    with open(f"./screenshot/{style}.png", "wb") as file:
        file.write(highlight(code, lexer, formatter))
