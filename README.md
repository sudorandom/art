Art
===
This is an extremely silly project where I use code to generate what some may consider art. The scripts are outlined below:

- `quine-hex.py` - This script will read its own source code as input and generate an image of the source code with hex-encoding. It also highlights certain letters to spell the word "QUINE". A quine is a program which produces a copy of its own source code as the output. In this case, the source code is outputted in the form of an image. It is possible to transcribe the hexadecimal back into runnable python code. [output](images/quine-hex.png)
- `quine-bin.py` - This script works exactly the same as `quine-hex.py` but instead of producing hexadecimal text, it produces binary... so it will be a page full of ones and zeros. [output](images/quine-bin.png)
- `random-hex.py` - This script generates random data and encodes it onto an image in hexadecimal format. Letters are highlighted to spell the word "RANDOM". [output](images/random-hex.png)
