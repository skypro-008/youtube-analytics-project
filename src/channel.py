import json
import os

from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

# Создаем переменную для API-ключа.
# API_KEY: str = os.getenv('YT_API_KEY')

# создать специальный объект для работы с API
# youtube = build('youtube', 'v3', developerKey=API_KEY)

# api_key = API_KEY
# channel_id = "UC-OVMPlMA3-YCIeg4z5z23A"


class Channel:
    """Класс для ютуб-канала"""
    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    @property
    def id(self):
        data_youtube = self.error_handler()
        return data_youtube["items"][0]["id"]

    @property
    def title(self):
        data_youtube = self.error_handler()
        return data_youtube["items"][0]["snippet"]["title"]

    @property
    def description(self):
        data_youtube = self.error_handler()
        return data_youtube["items"][0]["snippet"]["description"]

    @property
    def url(self):
        data_youtube = self.error_handler()
        return data_youtube["items"][0]["snippet"]["thumbnails"]["default"]["url"]

    @property
    def subscriberCount(self):
        data_youtube = self.error_handler()
        return data_youtube["items"][0]["statistics"]["subscriberCount"]

    @property
    def video_Count(self):
        data_youtube = self.error_handler()
        return data_youtube["items"][0]["statistics"]["videoCount"]

    @property
    def viewCount(self):
        data_youtube = self.error_handler()
        return data_youtube["items"][0]["statistics"]["viewCount"]

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        data_youtube = json.dumps(self.error_handler(), indent=2, ensure_ascii=False)
        print(data_youtube)

    # def to_json(self, name_file_json):

    def error_handler(self):
        try:
            channel = Channel.get_service().channels().list(id=self.channel_id, part='snippet,statistics').execute()
            # channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
            with open('channel_data.json', 'w', encoding='utf-8') as json_file:
                # Проверка на то, что данные успешно получены и сохранены в файл channel_data.json
                json.dump(channel, json_file, ensure_ascii=False, indent=2)
            # Открываем и читаем вновь созданный файл
            with open('channel_data.json', 'r', encoding='utf-8') as json_file:
                data_youtube = json.load(json_file)
            return data_youtube
        except Exception as e:
            try:
                with open('channel_data.json', 'r', encoding='utf-8') as json_file:
                    data_youtube = json.load(json_file)
                    print(f"Произошла ошибка при обращении к YouTube API: {e},\n"
                          "но данные успешно считаны из файла 'channel_data.json':")
                    return data_youtube
            except FileNotFoundError as er:
                print(f"Произошла ошибка при обращении к YouTube API: {er},\n"
                      "и не найден локальный файл с данными 'channel_data.json'.")
            except json.JSONDecodeError as je:
                print(f"Произошла ошибка при обращении к YouTube API: {je},\n"
                      "локальный файл 'channel_data.json' найден, но\n"
                      "произошла ошибка при декодировании данных из файла JSON: {je}")


channel = Channel('UC-OVMPlMA3-YCIeg4z5z23A')

# print(Channel.get_service())
print(channel.title)
print(channel.description)
print(channel.id)
print(channel.url)
print(channel.subscriberCount)
print(channel.video_Count)
print(channel.viewCount)
channel.print_info()
