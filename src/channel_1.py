import os
import json
#from distutils.command.build import build
from googleapiclient.discovery import build


api_key: str = os.getenv('UC-OVMPlMA3-YCIeg4z5z23A')
class Channel:
    """Класс для ютуб-канала"""


    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        youtube = build('youtube', 'v3', developerKey=api_key)
        self.response = youtube.channels().list(
            part='snippet,contentDetails,statistics',
            id=channel_id
        ).execute()

        # Обработка полученного результата
        self.channel = self.response['items'][0]
        self.snippet = self.channel['snippet']
        self.statistics = self.channel['statistics']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        # Формирование нужного формата данных
        data = {
            "kind": "youtube#channelListResponse",
            "etag":  {
        "title": "MoscowPython",
        "description": "Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)\nПрисоединяйтесь: https://www.facebook.com/groups/MoscowDjango! :)",
        "customUrl": "@moscowdjangoru",
        "publishedAt": "2012-07-13T09:48:44Z",
        "thumbnails": {
          "default": {
            "url": "https://yt3.ggpht.com/ytc/AGIKgqNv2rZ6mOSuXvJLYhmTc0nd-LtI5RiDtsEBpguJXA=s88-c-k-c0x00ffffff-no-rj",
            "width": 88,
            "height": 88
          },
          "medium": {
            "url": "https://yt3.ggpht.com/ytc/AGIKgqNv2rZ6mOSuXvJLYhmTc0nd-LtI5RiDtsEBpguJXA=s240-c-k-c0x00ffffff-no-rj",
            "width": 240,
            "height": 240
          },
          "high": {
            "url": "https://yt3.ggpht.com/ytc/AGIKgqNv2rZ6mOSuXvJLYhmTc0nd-LtI5RiDtsEBpguJXA=s800-c-k-c0x00ffffff-no-rj",
            "width": 800,
            "height": 800
          }
        },
        "localized": {
          "title": "MoscowPython",
          "description": "Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)\nПрисоединяйтесь: https://www.facebook.com/groups/MoscowDjango! :)"
        },
        "country": "RU"
      },
      "statistics": {
        "viewCount": "2303120",
        "subscriberCount": "25900",
        "hiddenSubscriberCount": False,
        "videoCount": "685"
      }
    }

        #Вывод результатов
        print(json.dumps(data, indent=2, ensure_ascii=False))