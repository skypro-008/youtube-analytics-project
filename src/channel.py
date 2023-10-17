import json
from helper.youtube_api_manual import youtube


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str, title: str = "", description: str = "", url: str = "",
                 subscriberCount: str = "", video_count: str = "", viewCount: str = "") -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self._channel_id = channel_id
        channel = youtube.channels().list(id=self._channel_id, part='snippet,statistics').execute()
        self.title = channel["items"][0]["snippet"]["title"]
        self.description = channel["items"][0]["snippet"]["description"]
        self.url = channel["items"][0]["snippet"]["thumbnails"]["default"]["url"]
        self.subscriberCount = channel["items"][0]["statistics"]["subscriberCount"]
        self.video_count = channel["items"][0]["statistics"]["videoCount"]
        self.viewCount = channel["items"][0]["statistics"]["viewCount"]

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=self._channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))
        return channel

    @classmethod
    def get_service(cls):
        channel_only_id = cls('UC-OVMPlMA3-YCIeg4z5z23A')
        channel = channel_only_id.print_info()
        # channel_id = channel["items"][0]["id"]
        title = channel["items"][0]["snippet"]["title"]
        description = channel["items"][0]["snippet"]["description"]
        url = channel["items"][0]["snippet"]["thumbnails"]["default"]["url"]
        subscriberCount = channel["items"][0]["statistics"]["subscriberCount"]
        videoCount = channel["items"][0]["statistics"]["videoCount"]
        viewCount = channel["items"][0]["statistics"]["viewCount"]

        channel_full = channel_only_id
        channel_full.title = title
        channel_full.description = description
        channel_full.url = url
        channel_full.subscriberCount = subscriberCount
        channel_full.video_count = videoCount
        channel_full.viewCount = viewCount

        return channel_full

    def to_json(self, json_file):
        channel_dict = dict(id=self._channel_id,
                            title=self.title,
                            description=self.description,
                            url=self.url,
                            subscriberCount=self.subscriberCount,
                            videoCount=self.video_count,
                            viewCount=self.viewCount)

        channel_dict_json = json.dumps(channel_dict)
        with open(json_file, "a") as file:
            file.write(channel_dict_json + "\n")
