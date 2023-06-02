import os
from googleapiclient.discovery import build

API_KEY = os.getenv('YT_API_KEY')
YOUTUBE = build('youtube', 'v3', developerKey=API_KEY)
