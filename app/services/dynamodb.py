import os
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

mongo_url = os.getenv("MONGO_URL")
client = MongoClient(mongo_url)
db = client["orders"]  # Usa la base de datos 'orders'
cart_collection = db["carts"]

import random

def create_cart(user_id):
    cart_id = random.randint(1_000_000, 9_999_999)
    cart = {
        "id": cart_id,
        "user_id": user_id,
        "product_ids": []
    }
    cart_collection.insert_one(cart)
    return cart_id
