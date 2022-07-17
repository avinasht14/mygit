import pymongo
client = pymongo.MongoClient("mongodb+srv://avinashreddy:WmXqpd5L.4-9wc@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"avinash",
    "email" : "avinash.t14@gmail.com",
    "surname" : "talakola"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )