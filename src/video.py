from src.youtube import youtube


class Video:
    """
    Класс для работы с видосиками
    """

    def __init__(self, video_id: str):
        """
        Экземпляр инициализируется id клипа. Дальше все данные будут подтягиваться по API.
        :param: video_id - id клипа
        info - Вся информация взятая из API
        id - id клипа
        title - название клипа
        url - ссылка на клип
        view_count - количество просмотров клипа
        like_count - количество лайков клипа
        """
        self.id = None
        self.title = None
        self.url = None
        self.view_count = None
        self.like_count = None
        try:
            self.info = youtube.videos().list(part='id,snippet,contentDetails,statistics',
                                              fields='items(id, snippet(title),'
                                                     'contentDetails(duration),'
                                                     'statistics(viewCount,likeCount))',
                                              id=video_id).execute()
            self.id = video_id
            self.title = self.info['items'][0]['snippet']['title']
            self.url = "https://youtu.be/" + self.id
            self.view_count = self.info['items'][0]['statistics']['viewCount']
            self.like_count = self.info['items'][0]['statistics']['likeCount']
        except IndexError:
            self.id = video_id

    def __str__(self):
        return f'{self.title}'


class PLVideo(Video):
    """
    Класс - наследник класса Video.
    Для работы с видосиками в плейлистах
    """

    def __init__(self, video_id: str, playlist_id: str):
        """
        Экземпляр инициализируется от id клипа и id плейлиста. Дальше все данные будут подтягиваться по API.
        :param: video_id - id клипа
        :param: playlist_id - id плейлиста
        К свойствам класса родителя добавлено свойство:
        playlist_id: str - хранит переданный playlist_id
        """
        self.list_id = None
        self.url = None
        super().__init__(video_id)
        if self.title:
            self.list_id = playlist_id
            self.url = "https://youtu.be/" + video_id + '?list=' + self.list_id
