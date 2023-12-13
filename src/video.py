import isodate
from googleapiclient.discovery import build
import os
import dotenv

dotenv.load_dotenv()

youtube = build('youtube', 'v3', developerKey=os.getenv('YT_API_KEY'))


class Video:
    def __init__(self, channel_id):
        self.channel_id = channel_id
        self.video = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails', id=channel_id).execute()['items'][0]
        self.title = self.video["snippet"]["title"]
        self.url = f"https://www.youtube.com/channel/{channel_id}"
        self.video_count = self.video["statistics"]["viewCount"]
        self.count_views = self.video["statistics"]["likeCount"]

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, channel_id, play_list_id):
        super().__init__(channel_id)
        self.play_list_id = play_list_id

    def __str__(self):
        return self.title


playlist_videos = youtube.playlistItems().list(part='snippet, contentDetails',
                                               id='PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw').execute()

print(playlist_videos)

video_ids = [video['contentDetails']['videoId'] for video in playlist_videos['items']]

print(video_ids)

video_response = youtube.videos().list(part='contentDetails,statistics',
                                       id=','.join(video_ids)
                                       ).execute()

for video in video_response['items']:
    # YouTube video duration is in ISO 8601 format
    iso_8601_duration = video['contentDetails']['duration']
    duration = isodate.parse_duration(iso_8601_duration)
    print(duration)
