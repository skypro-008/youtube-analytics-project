import os
from googleapiclient.discovery import build
import datetime
import json


class PlayList:
    def __init__(self, playlist_id):
        self.__playlist_id = playlist_id
        self.__api_key = os.getenv('YT_API_KEY')
        self.__youtube = build('youtube', 'v3', developerKey=self.__api_key)
        self.__playlist_videos = self.__youtube.playlistItems().list(
            playlistId=self.__playlist_id, part='contentDetails',
            maxResults=50, ).execute()
        self.title = None
        self.url = f"https://www.youtube.com/playlist?list={self.__playlist_id}"


def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


api_key = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)

playlist_id = 'PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw'
playlist_videos = youtube.playlistItems().list(
    playlistId=playlist_id, part='contentDetails',
    maxResults=50, ).execute()
printj(playlist_videos)

# playlist_id = 'PLH-XmS0lSi_zdhYvcwUfv0N88LQRt6UZn'
# playlist_videos = youtube.playlistItems().list(
#     playlistId=playlist_id, part='contentDetails',
#     maxResults=50,).execute()
# printj(playlist_videos)
