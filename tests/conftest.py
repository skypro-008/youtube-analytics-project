# from unittest import mock
# import pytest
# from src.channel import Channel
#
#
# @pytest.fixture
# def channel_mock():
#     # Мок объекта youtube
#     youtube_mock = mock.Mock()
#     youtube_channels_mock = youtube_mock.channels.return_value.list.return_value
#     youtube_channels_mock.execute.return_value = {
#         'items': [{
#             'id': 'channel_id',
#             'snippet': {'title': 'Channel Title'},
#             'statistics': {'viewCount': 100, 'subscriberCount': 500}
#         }]
#     }
#     # Экземпляр класса Channel с моком объекта youtube
#     channel = Channel('channel_id')
#     channel.channel = youtube_channels_mock.execute.return_value
#     return channel
