from flask import Flask, request
import json, numpy as np
from custom_modules import Mapdata, OCR

documents_list = []
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_vision():
    return "Vision Flask Server Working..."


@app.route('/mapdata/<station>',methods=['GET'])
def getMapdata(station):
    """
    station의 Sector 정보 반환
    return : JSON Array
    """
    results = Mapdata.readCollection(station)

    for result in results:
        result['_id'] = str(result['_id'])
        documents_list.append(result)

    collection_to_string = json.dumps(documents_list)
    return collection_to_string


@app.route('/ocr',methods=['POST'])
def getOCRtext():
    """
    Optical character recognition
    request : { "data" : ByteArray } 
    response : JSON
    """
    req = request.get_json()

    # bytes 변환은 unsigned Array만 가능, numpy 사용, java에서 unsigned 타입이 없어서.. 서버에서 해결
    byteImage = bytes(np.array(req["data"],dtype=np.uint8))
    ocrText = OCR.ByteImageToString(byteImage)

    return { "text" : ocrText }


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')