import requests

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.api_key = 'AIzaSyBZ76ebMl_GDynQb9wNWbIvrREj4J3mISQ'

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        url = f'https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={self.channel_id}&key={self.api_key}'
        response = requests.get(url)
        data = response.json()

        if 'items' in data:
            channel_info = data['items'][0]
            snippet = channel_info['snippet']
            statistics = channel_info['statistics']

            print({
                "title": snippet['title'],
                "description": snippet['description'],
                "subscriberCount": statistics['subscriberCount'],
                "viewCount": statistics['viewCount'],
                "videoCount": statistics['videoCount']
            })
