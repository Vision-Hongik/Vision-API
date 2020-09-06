from pymongo import MongoClient
from werkzeug.utils import secure_filename
import json
from bson.json_util import dumps

# client = MongoClient('mongodb://admin:vision1234@localhost:27017/') #mongodb와 연결
client = MongoClient() #mongodb와 연결
db = client.Mapdata #db이름 mapdata로 db 호출
collection = db.sangsu #collection 이름 info를 호출

results = collection.find() ### print(results) 의 결과는 내용이 아닌 <pymongo.cursor.Cursor object>

#내용을 출력하려면 for문 활용
for result in results:
    print(result)