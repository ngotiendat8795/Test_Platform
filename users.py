from pymongo import MongoClient
from faker import Faker
from random import randint, choice
from bson.objectid import ObjectId
faker = Faker()

mongo_uri = "mongodb+srv://admin:admin@c4e28cluster-chzuv.mongodb.net/test?retryWrites=true"


# 1. Connect to cluster

client = MongoClient(mongo_uri)

# 2. Get / Create database db_users và db_tests

db = client.db_ielts # đằng sau dấu chấm là tên database để đặt. Nếu đã tồn tại db thì sẽ get về lưu vào biến, nếu chưa thì sẽ tạo mới.

# 3. Get / Create collection

users = db["User_Data"]
