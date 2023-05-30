""" channel class module """
import json

from googleapiclient.discovery import build  # pylint: disable=E0401

from src.constants import API_KEY


class Channel:
    """Class for a YouTube channel"""

    __youtube = build(
        'youtube',
        'v3',
        developerKey=API_KEY
    )

    def __init__(self, channel_id: str) -> None:
        """
        Initializes an instance with the channel ID.
        Further data will be fetched through the API.

        Args:
            channel_id (str): The ID of the YouTube channel.
        """
        youtube_channel = 'https://www.youtube.com/channel/'
        self.__channel_id: str = channel_id
        self.__channel_title: str = self._snippet['title']
        self.__channel_description: str = self._snippet['description']
        self.__channel_url: str = youtube_channel + self.__channel_id

        self.__channel_subs: int = self._to_int(
            self._statistics['subscriberCount']
        )

        self.__channel_total_video: int = self._to_int(
            self._statistics['videoCount']
        )

        self.__channel_total_views = self._to_int(
            self._statistics['viewCount']
        )

    def __str__(self) -> str:
        """
        Returns a string representation of the object.

        Returns:
            str: The string representation of the object in the format:
            "{channel_title} ({channel_url})"
        """
        return f"{self.__channel_title} ({self.__channel_url})"

    def __add__(self, other) -> int:
        """
        Adds the number of subscribers of two channels.

        Args:
            other (Channel): The other Channel object to add.

        Returns:
            int: The sum of the number of subscribers of self and other.
        """
        return self.subscribers + other.subscribers

    def __sub__(self, other) -> int:
        """
        Subtracts the number of subscribers of two channels.

        Args:
            other (Channel): The other Channel object to subtract.

        Returns:
            int: The difference between the number of subscribers of
            self and other.
        """
        return self.subscribers - other.subscribers

    def __lt__(self, other) -> bool:
        """
        Checks if the number of subscribers of self is less than the
        number of subscribers of another channel.

        Args:
            other (Channel): The other Channel object to compare.

        Returns:
            bool: True if self has fewer subscribers than other, False
            otherwise.
        """
        return self.subscribers < other.subscribers

    def __le__(self, other) -> bool:
        """
        Checks if the number of subscribers of self is less than or
        equal to the number of subscribers of another channel.

        Args:
            other (Channel): The other Channel object to compare.

        Returns:
            bool: True if self has fewer or equal subscribers to other,
            False otherwise.
        """
        return self.subscribers <= other.subscribers

    def __gt__(self, other) -> bool:
        """
        Checks if the number of subscribers of self is greater than the
        number of subscribers of another channel.

        Args:
            other (Channel): The other Channel object to compare.

        Returns:
            bool: True if self has more subscribers than other, False
            otherwise.
        """
        return self.subscribers > other.subscribers

    def __ge__(self, other) -> bool:
        """
        Checks if the number of subscribers of self is greater than or
        equal to the number of subscribers of another channel.

        Args:
            other (Channel): The other Channel object to compare.

        Returns:
            bool: True if self has more or equal subscribers to other,
            False otherwise.
        """
        return self.subscribers >= other.subscribers

    def __eq__(self, other) -> bool:
        """
        Checks if the number of subscribers of self is equal to the
        number of subscribers of another channel.

        Args:
            other (Channel): The other Channel object to compare.

        Returns:
            bool: True if self has the same number of subscribers as
            other, False otherwise.
        """
        return self.subscribers == other.subscribers

    def __ne__(self, other) -> bool:
        """
        Checks if the number of subscribers of self is not equal to the
        number of subscribers of another channel.

        Args:
            other (Channel): The other Channel object to compare.

        Returns:
            bool: True if self has a different number of subscribers
            than other, False otherwise.
        """
        return self.subscribers != other.subscribers

    def print_info(self) -> None:
        """
        Prints information about the channel to the console.
        """
        self._printj(self._channel_info)

    @property
    def _channel_info(self) -> dict:
        """
        Returns the information about the YouTube channel.

        Returns:
            dict: The channel information including snippet and
            statistics.
        """
        result: dict = self.__youtube.channels().list(
            part='snippet,statistics',
            id=self.__channel_id
        ).execute()
        return result['items'][0]

    @staticmethod
    def _printj(dict_to_print: dict) -> None:
        """
        Prints a dictionary in a JSON-like format with indentation.

        Args:
            dict_to_print (dict): The dictionary to print.
        """
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls) -> object:
        """
        Returns the YouTube API service.

        Returns:
            googleapiclient.discovery.Resource: The YouTube API service.
        """
        return cls.__youtube

    @property
    def channel_id(self) -> str:
        """
        Returns the channel ID.

        Returns:
            str: The channel ID.
        """
        return self.__channel_id

    @property
    def title(self) -> str:
        """
        Returns the channel title.

        Returns:
            str: The channel title.
        """
        return self.__channel_title

    @property
    def description(self) -> str:
        """
        Returns the channel description.

        Returns:
            str: The channel description.
        """
        return self.__channel_description

    @property
    def url(self) -> str:
        """
        Returns the channel URL.

        Returns:
            str: The channel URL.
        """
        return self.__channel_url

    @property
    def subscribers(self) -> int:
        """
        Returns the number of channel subscribers.

        Returns:
            int: The number of channel subscribers.
        """
        return self.__channel_subs

    @property
    def video_count(self) -> int:
        """
        Returns the total number of videos on the channel.

        Returns:
            int: The total number of videos on the channel.
        """
        return self.__channel_total_video

    @property
    def views(self) -> int:
        """
        Returns the total number of channel views.

        Returns:
            int: The total number of channel views.
        """
        return self.__channel_total_views

    def to_json(self, file_title: str) -> None:
        """
        Saves the channel object as a JSON file.

        Args:
            file_title (str): The file name for the JSON file.
        """
        all_attrib = {
            "id": self.__channel_id,
            "title": self.__channel_title,
            "description": self.__channel_description,
            "url": self.__channel_url,
            "subscriberCount": self.__channel_subs,
            "videoCount": self.__channel_total_video,
            "viewCount": self.__channel_total_views
        }

        with open(
                file_title, 'w', encoding='utf-8'
        ) as filename:
            json.dump(all_attrib, filename, indent=2, ensure_ascii=False)

    @staticmethod
    def _to_int(string_num: str) -> int:
        """
        Converts a string representation of a number to an integer.

        Args:
            string_num (str): The string representation of a number.

        Returns:
            int: The converted integer value.
        """
        return int(float(string_num))

    @property
    def _snippet(self) -> dict:
        """
        Returns the snippet information of the YouTube channel.

        Returns:
            dict: The snippet information of the channel.
        """
        return self._channel_info['snippet']

    @property
    def _statistics(self) -> dict:
        """
        Returns the statistics information of the YouTube channel.

        Returns:
            dict: The statistics information of the channel.
        """
        return self._channel_info['statistics']

    def __repr__(self) -> str:
        """
        Returns a string representation of the channel.

        Returns:
            str: The channel ID.
        """
        return f"{self.__channel_id}"
