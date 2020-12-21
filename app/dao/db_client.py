from pymongo import MongoClient
import logging

from config.config import *

client = MongoClient(get_mongo_connect_string())
db = client.get_default_database()


def get_user_by_name(name):
    return db.user.find_one({"name": name})


def add_user(name):
    new_user = {"name": name}
    x = db.user.insert_one(new_user)

    return x.inserted_id


