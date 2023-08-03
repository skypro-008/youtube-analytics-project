import os

from googleapiclient.discovery import build


api_key: str = os.getenv('YT_API_KEY')
# Создаем объект работы с API
youtube = build('youtube', 'v3', developerKey=api_key)
