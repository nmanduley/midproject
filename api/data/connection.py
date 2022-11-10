from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

client = MongoClient(os.getenv("url"))
confirmed_global = client.get_database("confirmed_global")
deaths_global = client.get_database("deaths_global")
recovered_global = client.get_database("recovered_global")
print('hola')