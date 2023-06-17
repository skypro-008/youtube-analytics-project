import os
from googleapiclient.discovery import build


class YoutubeObject:
    service_name = 'youtube'
    service_version = 'v3'
    api_key = os.getenv('YT_API_KEY')
    service = build(service_name, service_version, developerKey=api_key)

    @classmethod
    def get_service(cls):
        return cls.service