import pymongo


class my_database:
    myclient = pymongo.MongoClient("mongodb://db_manager:Admin1234@localhost:27017/")
    mydb =  myclient["mydatabase"]
    colcounter = mydb["counter"]


def add_order(dict):
    cursor = my_database.colcounter.find()#.sort([('timestamp', -1)]).limit(1)
    latest_order = 0
    for x in cursor:
        latest_order = x['x']
    x = my_database.colcounter.insert_one({'x' : latest_order + 1})
    dict['ID'] = latest_order + 1
    mycol = my_database.mydb["orders"] #chestia cu client.ID de implementat in viitor
    x = mycol.insert_one(dict)
    
