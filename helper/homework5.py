from googleapiclient.discovery import build
from config import yt_api_key

youtube = build('youtube', 'v3', developerKey=yt_api_key)


def __get_data() -> dict:
    try:
        return youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                          id='asd'
                                          ).execute()
    except Exception as e:
        print(f'{e} : Несуществующий id')


print(__get_data())