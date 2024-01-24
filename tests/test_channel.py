from src.channel import Channel
import json
from googleapiclient.discovery import Resource


def test_channel_init():
    test_channel = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    assert test_channel.id == 'UC-OVMPlMA3-YCIeg4z5z23A'
    assert test_channel.title == 'MoscowPython'
    assert test_channel.url == 'https://www.youtube.com/UC-OVMPlMA3-YCIeg4z5z23A'


def test_get_service():
    assert isinstance(Channel.get_service(), Resource) is True


def test_to_json():
    test_data = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    test_data.to_json("test_data.json")

    with open('test_data.json', encoding="utf-8") as f:
        file_data = json.load(f)

    assert file_data.get("title") == test_data.title
    assert file_data.get("description") == test_data.description
    assert file_data.get("url") == test_data.url
