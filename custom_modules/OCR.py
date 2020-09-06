from flask import Flask, jsonify, request
import sys
from PIL import Image
import io
import pytesseract


def ByteImageToString(byteImage):
    # android -> server image 전송
    im = Image.open(io.BytesIO(byteImage))
    im.save("here.jpeg")
    
    #OCR
    detectedText = pytesseract.image_to_string(im, lang='kor', config='--psm 1 -c preserve_interword_spaces=1')
    completeText = detectedText.strip()
    print(completeText)

    return completeText

#안드로이드 연동 안되었을때 그냥 tesseract 결과만 확인하기 용도
def practiceOCR(path):
    targetImage = Image.open(path)
    
    #OCR
    detectedText = pytesseract.image_to_string(targetImage, lang='kor', config='--psm 1 -c preserve_interword_spaces=1')
    completeText = detectedText.strip()
    print(completeText)

    return completeText