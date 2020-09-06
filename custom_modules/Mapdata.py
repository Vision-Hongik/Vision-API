from pymongo import MongoClient
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import json
from bson.json_util import dumps

client = MongoClient() # 'mongodb://admin:vision1234@localhost:27017/'
db = client.Mapdata #db이름인 Mapdata로 db 호출

def readCollection(station):
    collection = db[station]
    resultObject = collection.find() 
    return resultObject