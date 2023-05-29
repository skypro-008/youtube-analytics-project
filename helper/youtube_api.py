import json
from dotenv import load_dotenv
import os
# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build
from src.video import Video, PLVideo

load_dotenv()

my_youtube_api_key = os.getenv("YT_API_KEY")
print(my_youtube_api_key)

youtube = build('youtube', 'v3', developerKey=my_youtube_api_key)

def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

playlist_id = 'PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb'

channel = youtube.channels().list(id='UCvuY904el7JvBlPbdqbfguw', part='snippet').execute()

playlist = youtube.playlists().list(part='snippet', id=playlist_id).execute()

playlist_videos = youtube.playlistItems().list(playlistId=playlist_id,
                                               part='contentDetails,snippet',
                                               maxResults=50,
                                               ).execute()

# print(json.dumps(playlist_videos, indent=1, ensure_ascii=False))
video_ids = [video['contentDetails']['videoId'] for video in playlist_videos['items']]

video_response = youtube.videos().list(part='contentDetails,statistics',
                                       id=','.join(video_ids)
                                       ).execute()
printj(video_response)