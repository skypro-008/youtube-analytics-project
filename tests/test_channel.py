import json
from unittest import mock
import pytest
from src.channel import Channel


@pytest.fixture
def channel_mock():
    # Мок объекта youtube
    youtube_mock = mock.Mock()
    youtube_channels_mock = youtube_mock.channels.return_value.list.return_value
    youtube_channels_mock.execute.return_value = {
        'items': [{
            'id': 'channel_id',
            'snippet': {'title': 'Channel Title'},
            'statistics': {'viewCount': 100, 'subscriberCount': 500}
        }]
    }
    # Экземпляр класса Channel с моком объекта youtube
    channel = Channel('channel_id')
    channel.channel = youtube_channels_mock.execute.return_value
    return channel


def test_channel_init(channel_mock):
    # Проверка, что инициализация экземпляра класса Channel проходит успешно
    assert channel_mock.channel_id == 'channel_id'
    assert channel_mock.channel == {
        'items': [{
            'id': 'channel_id',
            'snippet': {'title': 'Channel Title'},
            'statistics': {'viewCount': 100, 'subscriberCount': 500}
        }]
    }

def test_channel_print_info(channel_mock, capsys):
    # Проверка, что метод print_info выводит информацию о канале в консоль
    channel_mock.print_info()
    captured = capsys.readouterr()
    assert json.loads(captured.out) == {
        'items': [{
            'id': 'channel_id',
            'snippet': {'title': 'Channel Title'},
            'statistics': {'viewCount': 100, 'subscriberCount': 500}
        }]
    }