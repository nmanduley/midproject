from pymongo import MongoClient
from dotenv import load_dotenv
import os
from Routers import endpoints
load_dotenv()

client = MongoClient(os.getenv("url"))
covid = client.get_database("covid")
confirmed_global = covid["confirmed_global"]
deaths_global = covid["deaths_global"]
recovered_global = covid["recovered_global"]