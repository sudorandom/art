from PIL import Image, ImageDraw, ImageFont
import binascii
import math
import textwrap

width = 2900
height = 4060
padding = 200
effective_width = width - (padding*2)
effective_height = height - (padding*2)
y_padding = 5
font_path = "fonts/ApercuMono.ttf"

def calc_font(d, s):
    for font_size in reversed(range(40)):
        font = ImageFont.truetype(font=font_path, size=font_size)
        char_w, char_h = font.getsize("a")
        chars_per_line = int(effective_width / char_w)
        line_count = (effective_height / (char_h+y_padding))
        if chars_per_line * line_count > len(s):
            return {'font': font, 'char_w': char_w, 'char_h': char_h, 'line_count': line_count, 'chars_per_line': chars_per_line}

def dot(d, mtx, dt, x, y):
    d.text((padding+(dt['char_w']*x), (padding+((y_padding+dt['char_h'])*y))), mtx[y][x], font=dt['font'], fill="#eee")

byte_string = "0x"
with open(__file__, "rb") as f:
    byte_string += binascii.hexlify(f.read()).decode("utf-8")

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
    if len(chars) < chars_per_line:
        chars = chars + "0" * (chars_per_line - len(chars))
    mtx.append(chars)
    d.text((padding,offset), chars, font=dt['font'], fill="#444")
    offset += char_h+y_padding

ox = 20
oy = 10

# Q
dot(d, mtx, dt, ox+1, oy+0)
dot(d, mtx, dt, ox+2, oy+0)
dot(d, mtx, dt, ox+3, oy+0)
dot(d, mtx, dt, ox+0, oy+1)
dot(d, mtx, dt, ox+4, oy+1)
dot(d, mtx, dt, ox+0, oy+2)
dot(d, mtx, dt, ox+4, oy+2)
dot(d, mtx, dt, ox+0, oy+3)
dot(d, mtx, dt, ox+4, oy+3)
dot(d, mtx, dt, ox+0, oy+4)
dot(d, mtx, dt, ox+2, oy+4)
dot(d, mtx, dt, ox+4, oy+4)
dot(d, mtx, dt, ox+0, oy+5)
dot(d, mtx, dt, ox+3, oy+5)
dot(d, mtx, dt, ox+4, oy+5)
dot(d, mtx, dt, ox+1, oy+6)
dot(d, mtx, dt, ox+2, oy+6)
dot(d, mtx, dt, ox+3, oy+6)
dot(d, mtx, dt, ox+4, oy+6)

# U
ox+=7
dot(d, mtx, dt, ox+0, oy+0)
dot(d, mtx, dt, ox+4, oy+0)
dot(d, mtx, dt, ox+0, oy+1)
dot(d, mtx, dt, ox+4, oy+1)
dot(d, mtx, dt, ox+0, oy+2)
dot(d, mtx, dt, ox+4, oy+2)
dot(d, mtx, dt, ox+0, oy+3)
dot(d, mtx, dt, ox+4, oy+3)
dot(d, mtx, dt, ox+0, oy+4)
dot(d, mtx, dt, ox+4, oy+4)
dot(d, mtx, dt, ox+0, oy+5)
dot(d, mtx, dt, ox+4, oy+5)
dot(d, mtx, dt, ox+1, oy+6)
dot(d, mtx, dt, ox+2, oy+6)
dot(d, mtx, dt, ox+3, oy+6)

# I
ox+=7
dot(d, mtx, dt, ox+0, oy+0)
dot(d, mtx, dt, ox+1, oy+0)
dot(d, mtx, dt, ox+2, oy+0)
dot(d, mtx, dt, ox+3, oy+0)
dot(d, mtx, dt, ox+4, oy+0)
dot(d, mtx, dt, ox+2, oy+1)
dot(d, mtx, dt, ox+2, oy+2)
dot(d, mtx, dt, ox+2, oy+3)
dot(d, mtx, dt, ox+2, oy+4)
dot(d, mtx, dt, ox+2, oy+5)
dot(d, mtx, dt, ox+0, oy+6)
dot(d, mtx, dt, ox+1, oy+6)
dot(d, mtx, dt, ox+2, oy+6)
dot(d, mtx, dt, ox+3, oy+6)
dot(d, mtx, dt, ox+4, oy+6)

# N
ox+=7
dot(d, mtx, dt, ox+0, oy+0)
dot(d, mtx, dt, ox+4, oy+0)
dot(d, mtx, dt, ox+0, oy+1)
dot(d, mtx, dt, ox+4, oy+1)
dot(d, mtx, dt, ox+0, oy+2)
dot(d, mtx, dt, ox+1, oy+2)
dot(d, mtx, dt, ox+4, oy+2)
dot(d, mtx, dt, ox+0, oy+3)
dot(d, mtx, dt, ox+2, oy+3)
dot(d, mtx, dt, ox+4, oy+3)
dot(d, mtx, dt, ox+0, oy+4)
dot(d, mtx, dt, ox+3, oy+4)
dot(d, mtx, dt, ox+4, oy+4)
dot(d, mtx, dt, ox+0, oy+5)
dot(d, mtx, dt, ox+4, oy+5)
dot(d, mtx, dt, ox+0, oy+6)
dot(d, mtx, dt, ox+4, oy+6)

# E
ox+=7
dot(d, mtx, dt, ox+0, oy+0)
dot(d, mtx, dt, ox+1, oy+0)
dot(d, mtx, dt, ox+2, oy+0)
dot(d, mtx, dt, ox+3, oy+0)
dot(d, mtx, dt, ox+4, oy+0)
dot(d, mtx, dt, ox+0, oy+1)
dot(d, mtx, dt, ox+0, oy+2)
dot(d, mtx, dt, ox+0, oy+3)
dot(d, mtx, dt, ox+1, oy+3)
dot(d, mtx, dt, ox+2, oy+3)
dot(d, mtx, dt, ox+3, oy+3)
dot(d, mtx, dt, ox+0, oy+4)
dot(d, mtx, dt, ox+0, oy+5)
dot(d, mtx, dt, ox+0, oy+6)
dot(d, mtx, dt, ox+1, oy+6)
dot(d, mtx, dt, ox+2, oy+6)
dot(d, mtx, dt, ox+3, oy+6)
dot(d, mtx, dt, ox+4, oy+6)

out.save('quine-hex.png')
