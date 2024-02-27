from dotenv import load_dotenv

from src.channel import Channel

load_dotenv()


class Video(Channel):

    def __init__(self, video_id):
        self.video_id = video_id
        self.data_youtube = Channel.get_service().videos().list(part=
                         'snippet,statistics,contentDetails,topicDetails',
                         id=self.video_id
                         ).execute()

    @property
    def likecount(self):
        return self.data_youtube['items'][0]['statistics']['likeCount']


class PLVideo(Video):

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

    @property
    def playlist_videos(self):
        return Video.get_service().playlistItems().list(playlistId=self.playlist_id,
                                                                        part='contentDetails',
                                                                        maxResults=50,
                                                                        ).execute()

    @property
    def video_response(self):
        return Video.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                         id=self.video_id
                         ).execute()
    @property
    def id_playlist(self):
        return self.playlist_id


# video1 = Video('AWX4JnAnjBE')
# print(video1.data_youtube)
# print(video1.title)
# print(video1.video_id)
# print(video1.url)
# print(video1.viewCount)
# print(video1.likecount)
# print(str(video1))

# video2 = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')
# print(video2.playlist_videos)
# print()
# print(video2.video_response)
# print()
# print(video2.title)
# print()
# print(video2.video_id)
# print(video2.url)
# print(video2.viewCount)
# print(video2.likecount)
# print(f'id плейлиста: {video2.id_playlist}')
# print(str(video2))
