from src.apimixin import APIMixin


class Video(APIMixin):
    """Иницилизация через id и дальше по API"""
    def __init__(self, id_video):
        self.__id_video = id_video
        self._init_from_api()


    def _init_from_api(self):
        """Получаем данные по API и иницилизируем ими экземпляр класса"""
        video_response = self.get_service().videos().list(part='snippet,statistics',
                                                          id=self.__id_video
                                                          ).execute()

        self.video_title: str = video_response['items'][0]['snippet']['title']
        self.url = f'https://youtu.be/{self.__id_video}'
        self.view_count: int = video_response['items'][0]['statistics']['viewCount']
        self.like_count: int = video_response['items'][0]['statistics']['likeCount']


    def __str__(self):
        """Название видео"""
        return self.video_title



class PLVideo(Video):
    def __init__(self, id_video, id_playlist):
        super().__init__(id_video)
        self.id_playlist = id_playlist






