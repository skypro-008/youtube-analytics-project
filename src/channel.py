import os
import json
from googleapiclient.discovery import build


class Channel:
    def __init__(self, channel_id):
        self.id = channel_id
        self.title = None
        self.description = None
        self.custom_url = None
        self.published_at = None
        self.thumbnail_urls = {}
        self.country = None
        self.view_count = None
        self.subscriber_count = None
        self.video_count = None

        self.get_channel_info()

    def get_channel_info(self):
        api_key = os.getenv('YT_API_KEY') # Получение API-ключа из переменных окружения
        youtube = build('youtube', 'v3', developerKey=api_key)

        channel_data = youtube.channels().list(id=self.id, part='snippet,statistics').execute()

        if 'items' in channel_data and len(channel_data['items']) > 0:
            channel = channel_data['items'][0]
            snippet = channel.get('snippet', {})
            statistics = channel.get('statistics', {})

            self.title = snippet.get('title')
            self.description = snippet.get('description')
            self.custom_url = snippet.get('customUrl')
            self.published_at = snippet.get('publishedAt')
            self.thumbnail_urls = snippet.get('thumbnails', {})
            self.country = snippet.get('country')
            self.view_count = statistics.get('viewCount')
            self.subscriber_count = statistics.get('subscriberCount')
            self.video_count = statistics.get('videoCount')

    def get_channel_url(self):
        return f"https://www.youtube.com/channel/{self.id}"

    @classmethod
    def get_service(cls):
        api_key = os.getenv('YT_API_KEY')
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self, file_path):
        data = {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "custom_url": self.custom_url,
            "published_at": self.published_at,
            "thumbnail_urls": self.thumbnail_urls,
            "country": self.country,
            "view_count": self.view_count,
            "subscriber_count": self.subscriber_count,
            "video_count": self.video_count
        }

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)

    def print_info(self):
        print(f"Channel ID: {self.id}")
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Custom URL: {self.custom_url}")
        print(f"Published At: {self.published_at}")
        print(f"Thumbnail URLs: {self.thumbnail_urls}")
        print(f"Country: {self.country}")
        print(f"View Count: {self.view_count}")
        print(f"Subscriber Count: {self.subscriber_count}")
        print(f"Video Count: {self.video_count}")


