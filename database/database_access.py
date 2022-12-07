import pymongo
from pymongo import MongoClient
import sys

# allows us to go up a directory to import
sys.path.append('../national-football-predictor')
import keys

client = MongoClient(keys.mongo_url, tls = True, tlsAllowInvalidCertificates = True)

db = client['International_Football']

