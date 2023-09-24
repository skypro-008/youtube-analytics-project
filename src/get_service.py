from dataclasses import dataclass
import os
from googleapiclient.discovery import build


@dataclass
class Get_Service:
    """ Базовый класс для работы с API """
    YT_API_KEY = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=YT_API_KEY)
