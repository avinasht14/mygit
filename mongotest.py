import pymongo
client = pymongo.MongoClient("mongodb+srv://avinashreddy:avinash123@cluster0.hzqac.mongodb.net/?retryWrites=true&w=majority")
db = client.test

d = {
    "name":"avinash",
    "email" : "avinash.t14@gmail.com",
    "surname" : "reddy"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )