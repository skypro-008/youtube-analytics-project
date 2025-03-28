from src.channel import Channel

from dotenv import load_dotenv
import os
from googleapiclient.discovery import build
# Загружаем переменные из .env файла
load_dotenv()

# Получаем API-ключ
api_key = os.getenv('YT_API_KEY')
print(api_key)  # Для проверки, что ключ загружен

# Создаем клиент YouTube API
youtube = build('youtube', 'v3', developerKey=api_key)
# Пример запроса к API
request = youtube.channels().list(
    part='snippet,contentDetails,statistics',
    id='UC-OVMPlMA3-YCIeg4z5z23A'  # Замените на нужный ID канала
)
response = request.execute()

print(response)



if __name__ == '__main__':
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    moscowpython.print_info()

    """
{
  "kind": "youtube#channelListResponse",
  "etag": "uAdmwT0aDhY9LmAzJzIafD6ATRw",
  "pageInfo": {
    "totalResults": 1,
    "resultsPerPage": 5
  },
  "items": [
    {
      "kind": "youtube#channel",
      "etag": "cPh7A8SKcZxxs_UPCiBaXP1wNDk",
      "id": "UC-OVMPlMA3-YCIeg4z5z23A",
      "snippet": {
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
        "hiddenSubscriberCount": false,
        "videoCount": "685"
      }
    }
  ]
}

    """