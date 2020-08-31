from flask import Flask, render_template
from pymongo import MongoClient
import datetime
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import json
from bson.json_util import dumps

app = Flask(__name__)

client = MongoClient() #mongodb와 연결
db = client.mapdata #db이름 mapdata로 db 호출
collection = db.info #collection 이름 info를 호출

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('index.html')

#python script 따로
@app.route('/read',methods=['GET', 'POST'])
def mongoRead():
    # client = MongoClient('mongodb://admin:vision1234@localhost:27017/')
    results = collection.find() #json 통째로 보여주기
    client.close()
    temp = "["
    for i in results:
        i.pop('_id',None)
        i.pop('neighbor_sectors_id',None)
        temp += json.dumps(i)
        temp += ", "
    temp=temp[:-2]
    temp += "]"
    # print(type(temp))
    # print(temp)
    # jl = json.loads(temp)    
    # print(type(jl))
    # print(jl)
    # print(tuple(jl))
    return temp
    #return render_template('readdb.html', data=results)

@app.route('/remove', methods=['GET'])
def mongoDelete():
    collection.remove({"name": "sangsu3"}) #remove
    results = collection.find()
    
    return render_template('removedb.html', data=results)

@app.route('/update', methods=['GET'])
def mongoUpdate():
    collection.update({"name": "sangsu0"}, {"name": "sangsu0update"}, upsert=True) #update
    results = collection.find()
    
    return render_template('updatedb.html', data=results)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
