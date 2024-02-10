import json
import os

from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

# Создаем переменную для API-ключа.
API_KEY: str = os.getenv('YT_API_KEY')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=API_KEY)

# api_key = API_KEY
# channel_id = "UC-OVMPlMA3-YCIeg4z5z23A"


class Channel:
    """Класс для ютуб-канала"""
    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(self.error_handler())

    def error_handler(self):
        try:
            channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
            with open('channel_data.json', 'w', encoding='utf-8') as json_file:
                # Проверка на то, что данные успешно получены и сохранены в файл channel_data.json
                json.dump(channel, json_file, ensure_ascii=False, indent=2)
            # Открываем и читаем вновь созданный файл
            with open('channel_data.json', 'r', encoding='utf-8') as json_file:
                data_youtube = json.load(json_file)
                data_youtube = json.dumps(data_youtube, indent=2, ensure_ascii=False)
            return data_youtube
        except Exception as e:
            try:
                with open('channel_data.json', 'r', encoding='utf-8') as json_file:
                    data_youtube = json.load(json_file)
                    data_youtube = json.dumps(data_youtube, indent=2, ensure_ascii=False)
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
