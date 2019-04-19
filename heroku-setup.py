import json
import os
from boto.s3.connection import S3Connection
import main.KahunaBot

# Read the credentials file
filename = 'credentials/credentials.json'
with open(filename) as json_file:
    credentials = json.load(json_file)

#get useful things from environ variables
credentials["Token"] = str(os.environ['BotToken'])
credentials["ID"] = os.environ['ClientId']

#remove original file and export new credentials with correct token!
with open(filename, 'w') as outfile:
    json.dump(credentials, outfile)

#run bot - re do this later!!!
os.system("python3 main/KahunaBot.py")
