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

    def __init__(self, channel_id: str, data_youtube = {}) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.data_youtube = Channel.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute()

    @property
    def channel_id(self):
        return self.__channel_id

    @property
    def id(self):
        return self.data_youtube.get("items", [{}])[0].get("id", "")

    @property
    def title(self):
        return self.data_youtube.get("items", [{}])[0].get("snippet", {}).get("title", "")

    @property
    def description(self):
        return self.data_youtube.get("items", [{}])[0].get("snippet", {}).get("description", "")

    @property
    def url(self):
        return (self.data_youtube.get("items", [{}])[0].get("snippet", {}).get("thumbnails", {}).get("default", {})
                .get("url", ""))

    @property
    def subscriberCount(self):
        return self.data_youtube.get("items", [{}])[0].get("statistics", {}).get("subscriberCount", "")

    @property
    def video_Count(self):
        return self.data_youtube.get("items", [{}])[0].get("statistics", {}).get("videoCount", "")

    @property
    def viewCount(self):
        return self.data_youtube.get("items", [{}])[0].get("statistics", {}).get("viewCount", "")

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        data_youtube = json.dumps(self.data_youtube, indent=2, ensure_ascii=False)
        print(data_youtube)

    def to_json(self, name_file_json):  # = 'channel_atribut.json'):
        with open(f"{name_file_json}", "w", encoding='utf-8') as f:
            json.dump({"title": self.title,
                       "description": self.description,
                       "id": self.id,
                       "url": self.url,
                       "subscriberCount": self.subscriberCount,
                       "video_Count": self.video_Count,
                       "viewCount": self.viewCount}, f, ensure_ascii=False, indent=2)

    # def error_handler(self):
    #     try:
    #         # channel = Channel.get_service().channels().list(id=self.channel_id, part='snippet,statistics').execute()
    #         # youtube = self.get_service()
    #         # you_channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
    #         with open('channel_data.json', 'w', encoding='utf-8') as json_file:
    #             # Проверка на то, что данные успешно получены и сохранены в файл channel_data.json
    #             json.dump(you_channel, json_file, ensure_ascii=False, indent=2)
    #         # Открываем и читаем вновь созданный файл
    #         with open('channel_data.json', 'r', encoding='utf-8') as json_file:
    #             data_youtube = json.load(json_file)
    #         return data_youtube
    #     except Exception as e:
    #         try:
    #             with open('channel_data.json', 'r', encoding='utf-8') as json_file:
    #                 data_youtube = json.load(json_file)
    #                 print(f"Произошла ошибка при обращении к YouTube API: {e},\n"
    #                       "но данные успешно считаны из файла 'channel_data.json':")
    #                 return data_youtube
    #         except FileNotFoundError as er:
    #             print(f"Произошла ошибка при обращении к YouTube API: {er},\n"
    #                   "и не найден локальный файл с данными 'channel_data.json'.")
    #         except json.JSONDecodeError as je:
    #             print(f"Произошла ошибка при обращении к YouTube API: {je},\n"
    #                   "локальный файл 'channel_data.json' найден, но\n"
    #                   "произошла ошибка при декодировании данных из файла JSON: {je}")


# channel = Channel('UC-OVMPlMA3-YCIeg4z5z23A')

# print(Channel.get_service())
# print(channel.title)
# print(channel.description)
# print(channel.id)
# print(channel.subscriberCount)
# print(channel.video_Count)
# print(channel.viewCount)
# print(channel.url)
# channel.print_info()
# channel.to_json("jj.json")
