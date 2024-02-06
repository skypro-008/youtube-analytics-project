from googleapiclient.discovery import build

import isodate

API_KEY = "AIzaSyBq74XdWuXoBEsg3Guod5_BB8PTGYa6MWM"
api_key = API_KEY
channel_id = "UC-OVMPlMA3-YCIeg4z5z23A"

# class Channel:
#     """Класс для ютуб-канала"""
#
#     def __init__(self, channel_id: str) -> None:
#         """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
#         pass
#
#     def print_info(self) -> None:
#         """Выводит в консоль информацию о канале."""
#         pass


class Channel:
    """Class for working with YouTube channel data"""

    def __init__(self, api_key: str, channel_id: str) -> None:
        self.api_key = api_key
        self.channel_id = channel_id
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)

    def get_channel_info(self) -> dict:
        """Get information about the YouTube channel"""
        channel_data = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return channel_data

    def get_playlists(self) -> dict:
        """Get playlists of the YouTube channel"""
        playlists_data = self.youtube.playlists().list(channelId=self.channel_id, part='contentDetails,snippet', maxResults=50).execute()
        return playlists_data


# Инициализируем объект класса Channel с указанием api_key и channel_id
channel = Channel(api_key, channel_id)

# Получаем информацию о канале
channel_info = channel.get_channel_info()
print(channel_info)

# Получаем плейлисты канала
playlists_info = channel.get_playlists()
