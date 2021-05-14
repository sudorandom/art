from PIL import Image, ImageDraw, ImageFont
import binascii
import textwrap

width = 2900
height = 4060
padding = 200
effective_width = width - (padding*2)
effective_height = height - (padding*2)
y_padding = 5
font_path = "fonts/nk57-monospace-no-rg.ttf"

def calc_font(d, s):
    for font_size in range(40, 0, -1):
        font = ImageFont.truetype(font=font_path, size=font_size)
        char_w, char_h = font.getsize("a")
        chars_per_line = int(effective_width / char_w)
        line_count = (effective_height / (char_h+y_padding))
        if chars_per_line * line_count > len(s):
            return {'font': font, 'char_w': char_w, 'char_h': char_h, 'line_count': line_count, 'chars_per_line': chars_per_line}

def dot(d, mtx, dt, x, y):
    x_offset, _ = dt['font'].getsize("".join(mtx[y][0:x]))
    d.text((padding+x_offset, (padding+((y_padding+dt['char_h'])*y))), mtx[y][x], font=dt['font'], fill="#eee")

byte_string = ""
with open(__file__, "rb") as f:
    while True:
        byte = f.read(1)
        if not byte:
            break
        
        int_value = ord(byte)
        byte_string += '{0:08b}'.format(int_value)

out = Image.new("RGB", (width, height), (0, 0, 0))
d = ImageDraw.Draw(out)
dt = calc_font(d, byte_string)
char_w = dt['char_w']
char_h = dt['char_h']
chars_per_line = dt['chars_per_line']

mtx = []
offset = padding
for i in range(0, len(byte_string), chars_per_line):
    chars = byte_string[i:i + chars_per_line]
    mtx.append(chars)
    d.text((padding,offset), chars, font=dt['font'], fill="#444")
    offset += char_h+y_padding

ox = 20
oy = 10

letters = [
    # Q
    [(1, 0), (2, 0), (3, 0), (0, 1), (4, 1), (0, 2), (4, 2), (0, 3), (4, 3), (0, 4), (2, 4), (4, 4), (0, 5), (3, 5), (4, 5), (1, 6), (2, 6), (3, 6), (4, 6)],
    # U
    [(0, 0), (4, 0), (0, 1), (4, 1), (0, 2), (4, 2), (0, 3), (4, 3), (0, 4), (4, 4), (0, 5), (4, 5), (1, 6), (2, 6), (3, 6)],
    # I
    [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6)],
    # N
    [(0, 0), (4, 0), (0, 1), (4, 1), (0, 2), (1, 2), (4, 2), (0, 3), (2, 3), (4, 3), (0, 4), (3, 4), (4, 4), (0, 5), (4, 5), (0, 6), (4, 6)],
    # E
    [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (0, 4), (0, 5), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6)],
]

for letter in letters:
    ox+=7
    for (x, y) in letter:
        dot(d, mtx, dt, ox+x, oy+y)

out.save('images/quine-bin.jpg', dpi=(300, 300))

