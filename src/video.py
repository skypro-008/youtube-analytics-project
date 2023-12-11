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
