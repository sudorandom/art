import binascii
import PIL, PIL.Image, PIL.ImageDraw, PIL.ImageFont
import random

def chunks(seq, size):
  d, m = divmod(len(seq), size)
  for i in range(d):
    yield seq[i*size:(i+1)*size]
  if m:
    yield seq[d*size:]


def dump(binary, size=2, sep=' '):
  hexstr = binascii.hexlify(binary).decode('ascii')
  return sep.join(chunks(hexstr.upper(), size))

def dumpgen(data, length_per_line):
  '''
  Generator that produces strings:

  '00000000: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................'
  '''
  generator = chunks(data, length_per_line)
  for addr, d in enumerate(generator):
    # 00000000:
    line = '%08X: ' % (addr*length_per_line)
    # 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00 
    dumpstr = dump(d)
    line += dumpstr[:8*3]
    if len(d) > 8:  # insert separator if needed
      line += ' ' + dumpstr[8*3:]
    # ................
    # calculate indentation, which may be different for the last line
    pad = 2
    if len(d) < length_per_line:
      pad += 3*(length_per_line - len(d))
    if len(d) <= 8:
      pad += 1
    line += ' '*pad

    for byte in d:
      # printable ASCII range 0x20 to 0x7E
      if 0x20 <= byte <= 0x7E:
        line += chr(byte)
      else:
        line += '.'
    yield line


def main():
	random.seed(42)

	wake_up_text = 'Wake up, Neo'
	text_bytes = random.randbytes(100) + wake_up_text.encode() + random.randbytes(200)
	dump_str = '\n'.join(dumpgen(text_bytes, 16))

	out = PIL.Image.new("RGB", (4060, 2900), "#282828")
	d = PIL.ImageDraw.Draw(out)
	font = PIL.ImageFont.truetype(font="fonts/nk57-monospace-no-rg.ttf", size=71)
	d.multiline_text((200, 700), dump_str, font=font, fill="#888")
	d.text((3272, 1144), wake_up_text, font=font, fill="#66ff66")
	out.save('images/neo-dump-horizontal.jpg', dpi=(300, 300))

	dump_str = '\n'.join(dumpgen(text_bytes, 8))
	out2 = PIL.Image.new("RGB", (2900, 4060), "#282828")
	d = PIL.ImageDraw.Draw(out2)
	font2 = PIL.ImageFont.truetype(font="fonts/nk57-monospace-no-rg.ttf", size=80)
	d.multiline_text((250, 400), dump_str, font=font2, fill="#888")
	d.text((2410, 1396), "Wake", font=font2, fill="#66ff66")
	d.text((2248, 1480), "up, Neo", font=font2, fill="#66ff66")
	out2.save('images/neo-dump-vertical.jpg', dpi=(300, 300))

if __name__ == '__main__':
	main()
