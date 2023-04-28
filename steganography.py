from PIL import Image

def BinaryToDecimal(binary) :
    length = len(binary)
    res = 0
    for i in range(length) :
        res = res+int(binary[i])*2**(length-i-1)
    return res

png = Image.open("logo.png")
pixels = png.getdata()

bitsList = [0] * (len(pixels) * 4)

i = 0
for rgb in pixels :
    bitsList[i] = rgb[0] % 2
    i = i + 1
    bitsList[i] = rgb[1] % 2
    i = i + 1
    bitsList[i] = rgb[2] % 2
    i = i + 1
    bitsList[i] = rgb[3] % 2
    i = i + 1

charNb = len(bitsList)//8

f = open("message.txt","w")
for i in range(charNb) :
    f.write(chr(BinaryToDecimal(bitsList[8*i:8*(i+1)])))
f.close()