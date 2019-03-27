from pymongo import MongoClient
from datetime import datetime as dt

db = MongoClient(
    host='mongodb+srv://masai:kkkkk412@masai-vfhtb.mongodb.net/test?retryWrites=true', port=27017).masai
test_col = db['__dev_users']

test_col.insert({'_id' : dt.now().strftime("%Y-%m-%d-%H-%M-%S")})










