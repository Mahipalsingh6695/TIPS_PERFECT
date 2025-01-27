from pymongo import MongoClient

client = MongoClient("mongodb+srv://mahipalsinghchauhan1995:Mahi%406695@tipsg.8e47a.mongodb.net/?retryWrites=true&w=majority&appName=TipsG")
db = client["tipsG"]
results_collection = db["results"]
registration_collection = db["registrations"]