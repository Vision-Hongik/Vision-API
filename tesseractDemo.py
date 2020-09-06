import sys
from PIL import Image
from io import BytesIO
import pytesseract

with open("tess_data/star.png", "rb") as imageFile:
    f = imageFile.read()
    b = bytearray(f)


image_data = b
temp =BytesIO(image_data)
image = Image.open(temp)
image.save("hello.png")

# tmp = Image.open('tess_data/netp_textbook.jpg')
# # detectedText1 = pytesseract.image_to_string(tmp, lang='eng', config='--psm 1 -c preserve_interword_spaces=1')
# # completeText1 = detectedText1.strip()
# # print(completeText1)

# detectedText1 = pytesseract.image_to_string('samplebmp.bmp')
# completeText1 = detectedText1.strip()
# print(completeText1)
# # 한글 
# # print(pytesseract.image_to_string(Image.open('hangul.png'), lang='Hangul'))
