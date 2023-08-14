import os
import json
from googleapiclient.discovery import build

YT_API_KEY: str = os.getenv('YT_API_KEY')


def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


class Video:

    def __init__(self, id_video:str):
        self.__id_video = id_video
        self.load_video_yt()

    def load_video_yt(self):
        youtube = build('youtube', 'v3', developerKey=YT_API_KEY)
        # self.youtube_str = str(youtube)
        #
        # получить статистику видео по его id
        #
        # получить id можно из адреса видео https: // www.youtube.com / watch?v = gaoc9MPZ4bw
        # или https: // youtu.be / gaoc9MPZ4bw
        #
        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=self.__id_video).execute()
        printj(video_response)

        self.title: str = video_response['items'][0]['snippet']['title']
        self.url: str = 'https://www.youtube.com/watch?v=' + video_response['items'][0]['id']
        self.view_count: int = video_response['items'][0]['statistics']['viewCount']
        self.like_count: int = video_response['items'][0]['statistics']['likeCount']

    @property
    def id_video(self):
        return self.__id_video

    @id_video.setter
    def id_video(self, new_id):
        self.__id_video = new_id
        self.load_video_yt()


video1 = Video('AWX4JnAnjBE')