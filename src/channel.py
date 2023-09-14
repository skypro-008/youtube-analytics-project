import json
from googleapiclient.discovery import build


class Channel:
    def __init__(self, api_key: str, channel_id: str) -> None:
        self.api_key = api_key
        self.channel_id = channel_id
        self.youtube = self.get_service()
        self.channel_data = self.fetch_channel_data()

    def get_service(self):
        return build('youtube', 'v3', developerKey=self.api_key)

    def fetch_channel_data(self):
        request = self.youtube.channels().list(
            part='snippet,statistics',
            id=self.channel_id
        )
        response = request.execute()

        if 'items' in response:
            channel_info = response['items'][0]
            snippet = channel_info['snippet']
            statistics = channel_info['statistics']

            channel_data = {
                'id': self.channel_id,
                'title': snippet['title'],
                'description': snippet['description'],
                'link': f'https://www.youtube.com/channel/{self.channel_id}',
                'subscriberCount': int(statistics['subscriberCount']),
                'videoCount': int(statistics['videoCount']),
                'viewCount': int(statistics['viewCount']),
            }
            return channel_data
        else:
            return None

    def to_json(self, filename):
        if self.channel_data:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(self.channel_data, file, ensure_ascii=False, indent=4)

    def print_info(self):
        if self.channel_data:
            print("Channel ID:", self.channel_data['id'])
            print("Channel Name:", self.channel_data['title'])
            print("Description:", self.channel_data['description'])
            print("Link:", self.channel_data['link'])
            print("Subscriber Count:", self.channel_data['subscriberCount'])
            print("Video Count:", self.channel_data['videoCount'])
            print("View Count:", self.channel_data['viewCount'])
        else:
            print("Channel not found")


if __name__ == '__main__':
    api_key = 'AIzaSyDOsEBflTxbKq0zbiuwT1Tp53zY33WQmEI'
    channel_id = 'UC-OVMPlMA3-YCIeg4z5z23A'
    pythchannel = Channel(api_key, channel_id)
    pythchannel.print_info()
    pythchannel.to_json('channel_data.json')
