""" channel class module """
import json

from googleapiclient.discovery import build  # pylint: disable=E0401

from src.constants import API_KEY


class Channel:
    """Class for a YouTube channel"""

    youtube = build(
        'youtube',
        'v3',
        developerKey=API_KEY
    )

    def __init__(self, channel_id: str = None, channel_name: str = None) -> \
            None:
        """
        Initializes an instance with the channel ID.
        Further data will be fetched through the API.
        """
        self.channel_name = channel_name
        if self.channel_name:
            self.channel_id = self._get_channel_id_by_channel_name()
        else:
            self.channel_id = channel_id

    def print_info(self) -> None:
        """
        Prints information about the channel to the console.
        """

        result = self.youtube.channels().list(
            id=self.channel_id,
            part='snippet,statistics'
        ).execute()

        self._printj(result)

    def _get_channel_id_by_channel_name(self) -> str:
        """
        Retrieves the channel ID based on the channel name using
        the YouTube API.
        """
        channel_info = self.youtube.search().list(
            part='id,snippet',
            maxResults=1,
            type='channel',
            q=self.channel_name,
        ).execute()
        return channel_info['items'][0]['id']['channelId']

    @staticmethod
    def _printj(dict_to_print: dict) -> None:
        """
        Prints a dictionary in a JSON-like format with indentation
        """
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    def __repr__(self):
        """
        Return repr
        """
        return f"{self.channel_id}"
