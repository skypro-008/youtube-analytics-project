from src.channel import Channel

import pytest


@pytest.fixture
def channel1():
    return Channel('UC-OVMPlMA3-YCIeg4z5z23A')


def test_class_Channel_channel_id(channel1):
    assert channel1.channel_id == 'UC-OVMPlMA3-YCIeg4z5z23A'


def test_class_Channel_print_info(channel1):
    assert channel1.print_info() == {
        "kind": "youtube#channelListResponse",
        "etag": "uAdmwT0aDhY9LmAzJzIafD6ATRw",
        "pageInfo": {
            "totalResults": 1,
            "resultsPerPage": 5
        },
        "items": [
            {
                "kind": "youtube#channel",
                "etag": "cPh7A8SKcZxxs_UPCiBaXP1wNDk",
                "id": "UC-OVMPlMA3-YCIeg4z5z23A",
                "snippet": {
                    "title": "MoscowPython",
                    "description": "Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)\nПрисоединяйтесь: https://www.facebook.com/groups/MoscowDjango! :)",
                    "customUrl": "@moscowdjangoru",
                    "publishedAt": "2012-07-13T09:48:44Z",
                    "thumbnails": {
                        "default": {
                            "url": "https://yt3.ggpht.com/ytc/AGIKgqNv2rZ6mOSuXvJLYhmTc0nd-LtI5RiDtsEBpguJXA=s88-c-k-c0x00ffffff-no-rj",
                            "width": 88,
                            "height": 88
                        },
                        "medium": {
                            "url": "https://yt3.ggpht.com/ytc/AGIKgqNv2rZ6mOSuXvJLYhmTc0nd-LtI5RiDtsEBpguJXA=s240-c-k-c0x00ffffff-no-rj",
                            "width": 240,
                            "height": 240
                        },
                        "high": {
                            "url": "https://yt3.ggpht.com/ytc/AGIKgqNv2rZ6mOSuXvJLYhmTc0nd-LtI5RiDtsEBpguJXA=s800-c-k-c0x00ffffff-no-rj",
                            "width": 800,
                            "height": 800
                        }
                    },
                    "localized": {
                        "title": "MoscowPython",
                        "description": "Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)\nПрисоединяйтесь: https://www.facebook.com/groups/MoscowDjango! :)"
                    },
                    "country": "RU"
                },
                "statistics": {
                    "viewCount": "2303120",
                    "subscriberCount": "25900",
                    "hiddenSubscriberCount": 'false',
                    "videoCount": "685"
                }
            }
        ]
    }
