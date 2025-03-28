from googleapiclient.discovery import build
import json
class Channel:
    """Класс для ютуб-канала"""
    api_key: str = 'AIzaSyBpls0q5DFRSc6Nr6ZIIEvhjOYYi7yVH7s'
    youtube = build('youtube', 'v3', developerKey=api_key)
    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.__channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.youtube = self.get_service()  # Создаем объект YouTube API здесь

        if 'items' in self.__channel and len(self.__channel['items']) > 0:
            self.id = self.__channel['items'][0]['id']
            self.title = self.__channel['items'][0]['snippet']['title']
            self.description = self.__channel['items'][0]['snippet']['description']
            self.url = f"https://www.youtube.com/channel/{self.id}"
            self.subscriber_count = self.__channel['items'][0]['statistics']['subscriberCount']
            self.video_count = self.__channel['items'][0]['statistics']['videoCount']
            self.view_count = self.__channel['items'][0]['statistics']['viewCount']
        else:
            raise ValueError("Канал не найден или данные недоступны.")

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(self.__channel)

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API."""
        api_key = 'YT_API_KEY'
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self, filename: str) -> None:
        """Сохраняет данные о канале в JSON-файл."""
        channel_info = {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "subscriber_count": self.subscriber_count,
            "video_count": self.video_count,
            "view_count": self.view_count
        }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(channel_info, f, ensure_ascii=False, indent=2)

    def print_info(self) -> None:
        channel_info = {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "subscriber_count": self.subscriber_count,
            "video_count": self.video_count,
            "view_count": self.view_count
    }
        print(json.dumps(channel_info, indent=2, ensure_ascii=False))

    def __str__(self):
        return f"{self.title},  {self.url}"

    def __add__(self, other):
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __sub__(self, other):
        return int(other.subscriber_count) - int(self.subscriber_count)

    def __gt__(self, other):
        return int(self.subscriber_count) > int(other.subscriber_count)

    def __lt__(self, other):
        return int(self.subscriber_count) < int(other.subscriber_count)

    def __ge__(self, other):
        return int(self.subscriber_count) >= int(other.subscriber_count)

    def __le__(self, other):
        return int(self.subscriber_count) <= int(other.subscriber_count)

    def __eq__(self, other):
        return int(self.subscriber_count) == int(other.subscriber_count)
