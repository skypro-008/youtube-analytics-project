from googleapiclient.discovery import build


class Channel:

    def __init__(self,api_key: str, channel_id: str) -> None:
        self.api_key = api_key
        self.channel_id = channel_id
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)

    def print_info(self) -> None:
        request = self.youtube.channels().list(
            part='snippet,statistics',
            id=self.channel_id
        )
        response = request.execute()

        if 'items' in response:
            channel_info = response['items'][0]
            snippet = channel_info['snippet']
            statistics = channel_info['statistics']

            print("Channel Name:", snippet['title'])
            print("Description:", snippet['description'])
            print("Published At:", snippet['publishedAt'])
            print("Country:", snippet['country'])
            print("View Count:", statistics['viewCount'])
            print("Subscriber Count:", statistics['subscriberCount'])
            print("Video Count:", statistics['videoCount'])
        else:
            print("Channel not found")


if __name__ == '__main__':
    api_key = 'AIzaSyDOsEBflTxbKq0zbiuwT1Tp53zY33WQmEI'
    channel_id = 'UC-OVMPlMA3-YCIeg4z5z23A'
    pythchannel = Channel(api_key, channel_id)
    pythchannel.print_info()
