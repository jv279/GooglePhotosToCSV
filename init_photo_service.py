import os
from Google import Create_Service

API_NAME = 'photoslibrary'
API_VERSION = 'v1'
#This is personal for each user so I havent uploaded this secret file
CLIENT_SECRET_FILE = 'client_secret_googlephoto.json'
SCOPES = ['https://www.googleapis.com/auth/photoslibrary.readonly']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


# print(dir(service))