import datetime
import isodate
import os

from src.channel import Channel
from src.video import PLVideo


class PlayList:
    def __init__(self, pl_id):
        """Экземпляр инициализируется  id плейлиста.
        Дальше все данные будут подтягиваться по API."""
        self.pl_id = pl_id
        self.title = self.get_info()['items'][0]['snippet']['title']
        self.url = os.path.join('https://www.youtube.com/playlist?list=' + self.pl_id)

    def get_info(self):
        '''Возвращает коллекцию списков воспроизведения, соответствующих параметрам запроса API.
        Поиск по ID канала или плейлиста. Выход в разрезе плейлиста: contentDetails (кол-во видео в плейлисте) +
        snippet (title, description etc)'''
        return Channel.get_service().playlists().list(id=self.pl_id,
                                                      part='contentDetails, snippet',
                                                      maxResults=50,
                                                      ).execute()

    def get_pl_videos(self):
        '''Возвращает коллекцию элементов плейлиста, соответствующих параметрам запроса API.
        Выход в разрезе видео: contentDetails (только ID и дата публикации) +
        id, snippet, status'''
        return Channel.get_service().playlistItems().list(playlistId=self.pl_id,
                                                          part='contentDetails',
                                                          maxResults=50,
                                                          ).execute()

    def set_video_list(self):
        '''Возвращает список объектов класса PLVideo'''
        video_list = []
        for video in self.get_pl_videos()['items']:
            video_list.append(PLVideo(video['contentDetails']['videoId'], self.pl_id))
        return video_list

    @property
    def total_duration(self):
        return sum([isodate.parse_duration(video.duration) for video in self.set_video_list()],
                   datetime.timedelta(0))

        # total_duration = datetime.timedelta(0)
        # for video in self.set_video_list():
        #     video_duration = isodate.parse_duration(video.duration)
        #     total_duration += video_duration
        # return total_duration

    def show_best_video(self):
        video_list = self.set_video_list()
        max_likes = max(video.likes for video in video_list)
        best_video = ''.join(video.video_id for video in video_list
                             if video.likes == max_likes)
        return os.path.join('https://youtu.be/', best_video)

        # max_likes = 0
        # vd_id = ''
        # for video in self.set_video_list():
        #     if int(video.likes) > max_likes:
        #         max_likes = int(video.likes)
        #         vd_id = video.video_id
        # return os.path.join('https://youtu.be/', vd_id)
