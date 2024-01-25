from src.youtube import youtube
from src.video import Video
from datetime import timedelta
import isodate


class PlayList:
    """Класс работы с плейлистами"""

    def __init__(self, playlist_id: str):
        """
        Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API.
        :param: channel_id - Id канала
        info - Вся информация взятая из API
        id - id плейлиста
        title - название плейлиста
        url - ссылка на плейлист
        video_ids - список Id клипов в плейлисте
        """
        self.info = youtube.playlistItems().list(playlistId=playlist_id,
                                                 part='id,snippet,contentDetails',
                                                 fields='items(id,snippet(title,description,videoOwnerChannelId),'
                                                        'contentDetails(videoId))',
                                                 maxResults=50).execute()

        self.id = playlist_id
        self.url = "https://www.youtube.com/playlist?list=" + self.id
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.info['items']]
        self.title = self.get_playlist_title()

    def get_playlist_title(self) -> str:
        """
        Проктологически добываем Название плейлиста по его Id
        1 - Получаем Id канала где плейлист создан
        2 - Потом вытаскиваем список плейлистов канала
        3 - Выбираем из списка каналов нужный по Id
        4 - Достаем его название
        Научите делать проще
        :return: result: str - искомое название плейлиста
        """
        temp = youtube.playlists().list(channelId=self.info['items'][0]['snippet']['videoOwnerChannelId'],
                                        part='id,snippet',
                                        fields='items(id,snippet(title))',
                                        maxResults=50).execute()
        result = None
        for item in temp['items']:
            if item['id'] == self.id:
                result = item['snippet']['title']
        del temp
        return result

    @property
    def total_duration(self) -> timedelta:
        """
        Считаем продолжительность плейлиста
        1 - Получаем список свойств info объектов класса Video по списку Id из video_ids
        2 - Суммируем продолжительности клипов (преобразовываем из ISO 8601 в timedelta [isodate])
        :return: d: timedelta - Продолжительность плейлиста
        """
        video_list: list[dict] = [Video(video_id).info for video_id in self.video_ids]
        d = timedelta(microseconds=0)
        for video in video_list:
            d += isodate.parse_duration(video['items'][0]['contentDetails']['duration'])
        return d

    def show_best_video(self) -> str:
        """
        Считаем продолжительность плейлиста
        1 - Получаем список свойств info объектов класса Video по списку Id из video_ids
        2 - Ищем самый популярный клип из списка (по количеству лайков)
        3 - Сохраняем его Id
        :return: str - Ссылка на самый популярный клип в плейлисте
        """
        video_list: list[dict] = [Video(video_id).info for video_id in self.video_ids]
        max_result = 0
        result_id = ''
        for video in video_list:
            result = int(video['items'][0]['statistics']['likeCount'])
            if result > max_result:
                max_result = result
                result_id = video['items'][0]['id']
        return f'https://youtu.be/{result_id}'
