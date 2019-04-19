import json
import os
from boto.s3.connection import S3Connection
import ../main/KahunaBot

# Read the credentials file
filename = 'credentials/changeme.txt'
with open(filename) as json_file:
    credentials = json.load(json_file)

#get token from environ variables
credentials["Token"] = os.environ['BotToken']

#remove original file and export new credentials with correct token!
os.remove(filename)
with open(filename, 'w') as outfile:
    json.dump(credentials, outfile)

KahunaBot()
