import os
import json
import requests


class Channel:
    def __init__(self, channel_id):
        self.channel_id = channel_id
        self.title = None
        self.description = None
        self.url = None
        self.subscriber_count = None
        self.video_count = None
        self.view_count = None

        self.fetch_channel_info()  # Получаем информацию о канале

    def fetch_channel_info(self):
        api_key = os.environ.get("YouTube_API")

        if not api_key:
            print("API не найден.")
            return

        url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={self.channel_id}&key={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()

            channel_data = response.json()
            channel = channel_data.get("items", [{}])[0]

            self.title = channel.get("snippet", {}).get("title", "N/A")
            self.description = channel.get("snippet", {}).get("description", "N/A")
            self.url = f"https://www.youtube.com/channel/{self.channel_id}"
            self.subscriber_count = channel.get("statistics", {}).get("subscriberCount", "N/A")
            self.video_count = channel.get("statistics", {}).get("videoCount", "N/A")
            self.view_count = channel.get("statistics", {}).get("viewCount", "N/A")

        except requests.exceptions.HTTPError as errh:
            print("HTTP Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print("Something went wrong:", err)

    @classmethod
    def get_service(cls):
        # получение объекта для работы с YouTube API
        return "<googleapiclient.discovery.Resource object>"

    def to_json(self, filename):
        data = {
            "id": self.channel_id,
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "subscriber_count": self.subscriber_count,
            "video_count": self.video_count,
            "view_count": self.view_count
        }

        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

if __name__ == '__main__':
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')

    # значения атрибутов
    print(moscowpython.title)  # Выводим название канала
    print(moscowpython.video_count)  # Выводим количество видео
    print(moscowpython.url)  # Выводим ссылку на канал

    # Пробуем изменить атрибут
    moscowpython.channel_id = 'Новое название'
    # AttributeError: can't set attribute

    # Полкчаем объект для работы с API вне класса
    print(Channel.get_service())

    # Создаем файл 'moscowpython.json' с данными по каналу
    moscowpython.to_json('moscowpython.json')
