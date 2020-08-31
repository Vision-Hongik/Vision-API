from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import json

app = Flask(__name__)


# OpenCv image Frame울 받아 출력해본다.
@app.route('/post', methods=['POST'])
def test():
    print(request.json)

    return dict({"hello":"hello"})



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
