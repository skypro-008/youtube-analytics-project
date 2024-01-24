
import os
from googleapiclient.discovery import build

api_key: str = os.getenv('YOUTUBEAPIKEY')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)