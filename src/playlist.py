import datetime
import isodate
from googleapiclient.discovery import build
from src.constants import API_KEY
from src.video import Video

class PlayList:
    """
    Represents a YouTube playlist.

    Attributes:
        playlist_id (str): The ID of the playlist.
        __youtube (googleapiclient.discovery.Resource): The YouTube API resource object.
        _pl_title (str): The title of the playlist.
        _pl_url (str): The URL of the playlist.
        _pl_video_durations (list): The durations of the videos in the playlist.
    """

    __youtube = build('youtube', 'v3', developerKey=API_KEY)

    def __init__(self, playlist_id):
        """
        Initializes a PlayList object.

        Args:
            playlist_id (str): The ID of the playlist.
        """
        youtube_url = 'https://www.youtube.com/playlist?list='
        self.playlist_id = playlist_id
        self._pl_title = self.playlist['snippet']['title']
        self._pl_url = youtube_url + self.playlist_id
        self._pl_video_durations = self._video_duration

    @property
    def total_duration(self):
        """
        Calculates the total duration of the playlist.

        Returns:
            datetime.timedelta: The total duration of the playlist.
        """
        return sum(self._video_duration, datetime.timedelta())

    @property
    def _playlist_video_ids(self):
        """
        Retrieves the video IDs of the playlist.

        Returns:
            list: A list of video IDs in the playlist.
        """
        playlist_content = self.__youtube.playlistItems().list(
            playlistId=self.playlist_id,
            part='contentDetails',
        ).execute()
        video_ids = [
            video['contentDetails']['videoId']
            for video in playlist_content['items']
        ]
        return video_ids

    @property
    def _video_duration(self):
        """
        Retrieves the durations of the videos in the playlist.

        Returns:
            list: A list of durations of the videos in the playlist.
        """
        videos = []
        for video in self._playlist_video_ids:
            videos.append(isodate.parse_duration(Video(video).duration))
        return videos

    @property
    def playlist(self):
        """
        Retrieves the playlist details.

        Returns:
            dict: A dictionary containing the details of the playlist.
        """
        result = self.__youtube.playlists().list(
            part='snippet',
            id=self.playlist_id
        ).execute()
        return result['items'][0]

    @property
    def title(self):
        """
        Retrieves the title of the playlist.

        Returns:
            str: The title of the playlist.
        """
        return self._pl_title

    @property
    def url(self):
        """
        Retrieves the URL of the playlist.

        Returns:
            str: The URL of the playlist.
        """
        return self._pl_url

    def show_best_video(self):
        """
        Finds the video with the most likes in the playlist.

        Returns:
            str: The URL of the video with the most likes in the playlist.
        """
        youtube_link = 'https://youtu.be/'
        result_url = ''
        most_liked = 0
        for video in self._playlist_video_ids:
            video_likes = Video(video).likes
            if video_likes > most_liked:
                most_liked = video_likes
                result_url = youtube_link + video

        return result_url
