import json
import os
from googleapiclient.discovery import build


YT_API_KEY: str = os.getenv('YT_API_KEY')
# JSON_FILE: str = '..\src\yt_channel.json'

def full_path_name_file(name_file):
    """
    формируем полный путь до файла
    :param name_file: имя файла с указанием подпапки
    :return: полный пусть в UNIX системы
    """
    # return os.getcwd() + '\\' + name_file
    # return os.path.join(*name_file.replace('\\','/').split('/'))
    # cur_path = os.path.dirname(__file__)
    return os.path.realpath(name_file)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        youtube = build('youtube', 'v3', developerKey=YT_API_KEY)
        self.__youtube = id(youtube)

        channel = youtube.channels().list(id=self.channel_id,
                                          part='snippet,statistics').execute()

        self.url: str = 'https://www.youtube.com/channel/'+channel['items'][0]['id']
        self.subscriber_count: str = channel["items"][0]["statistics"]["subscriberCount"]
        self.video_count: str = channel["items"][0]["statistics"]["videoCount"]
        self.view_count: str = channel["items"][0]["statistics"]["viewCount"]
        self.title: str = channel["items"][0]["snippet"]["title"]
        self.description: str = channel["items"][0]["snippet"]["description"]


    def __repr__(self):
        return f'id канала: {self.channel_id}\n' \
               f'название канала: {self.title}\n' \
               f'описание канала: {self.description}\n' \
               f'ссылка на канал: {self.url}\n' \
               f'количество подписчиков: {self.subscriber_count}\n' \
               f'количество видео: {self.video_count}\n' \
               f'общее количество просмотров: {self.view_count}'


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        # создать специальный объект для работы с API
        youtube = build('youtube', 'v3', developerKey=YT_API_KEY)

        channel = youtube.channels().list(id=self.channel_id,
                                          part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))


    def get_service(self):
        return self.__youtube


    def to_json(self, name_file: str):
        json_list = {"id": self.channel_id,
                     "title": self.title,
                     "description": self.description,
                     "url": self.url,
                     "subscriberCount": self.subscriber_count,
                     "videoCount": self.video_count,
                     "viewCount": self.view_count
                     }

        name_file = full_path_name_file(name_file)
        with open(name_file, 'w', encoding='UTF-8') as file:
            json.dumps(json_list, file)
