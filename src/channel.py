import json
import os
from googleapiclient.discovery import build

import isodate


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        api_key: str = os.getenv('YT_API_KEY')
        # создать специальный объект для работы с API
        special_controller_yt = build('youtube', 'v3', developerKey=api_key)
        # channel_id = 'UC-OVMPlMA3-YCIeg4z5z23A'  # MoscowPython
        # channel_id = 'UCwHL6WHUarjGfUM_586me8w'  # HighLoad Channel
        self.channel_summary_info = special_controller_yt.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        # print(self.channel_summary_info)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(self.channel_summary_info)
#
#     def printj(dict_to_print: dict) -> None:
#         """Выводит словарь в json-подобном удобном формате с отступами"""
#         print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))
#
test_results = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
test_results.print_info()
# test_results.printj(test_results.print_info)
#
#
#
#
# '''
# получить данные о канале по его id
# docs: https://developers.google.com/youtube/v3/docs/channels/list
#
# сервис для быстрого получения id канала: https://commentpicker.com/youtube-channel-id.php
# '''




