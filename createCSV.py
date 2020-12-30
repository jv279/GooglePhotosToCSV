from os.path import supports_unicode_filenames
from init_photo_service import service
import pandas as pd 
import csv as csv

#Max page size for media items is 100
response = service.mediaItems().list(
    pageSize = 100
).execute()
lstmedia = response.get('mediaItems')

df_filenames = pd.DataFrame(lstmedia)

nextPageToken = response.get('nextPageToken')


"""
nextpageToken is a string that can reference the page after the current page
this while loop continues until the last page (no more next pages)

The response is best viewed in a dataframe due to the copius amounts of info
"""
while nextPageToken:
    response = service.mediaItems().list(
        pageSize=100,
        pageToken = nextPageToken 
    ).execute()
    
    nextPageToken = response.get('nextPageToken')
    
    newdata = response.get('mediaItems')
    newdf = pd.DataFrame(newdata)
    df_filenames = df_filenames.append(newdf)

#The output is sent to a CSV file called outputall.csv

df_filenames.to_csv('outputall.csv')
