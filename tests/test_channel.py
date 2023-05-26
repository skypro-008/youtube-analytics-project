""" Channel class testing module """
import os
from unittest.mock import patch

from src.channel import Channel


def test_channel_id(channel):
    """Test for the channel_id property of the Channel class."""
    assert channel.channel_id == 'UC-OVMPlMA3-YCIeg4z5z23A'


def test_channel_title(channel):
    """Test for the title property of the Channel class."""
    assert channel.title == 'MoscowPython'


def test_channel_description(channel):
    """Test for the description property of the Channel class."""
    assert channel.description == 'Видеозаписи со встреч питонистов и ' \
                                  'джангистов в Москве и не только. :)\n' \
                                  'Присоединяйтесь: https://www.facebook.com' \
                                  '/groups/MoscowDjango! :)'


def test_channel_url(channel):
    """Test for the url property of the Channel class."""
    assert channel.url == 'https://www.youtube.com/channel/UC-OVMPlMA3-' \
                          'YCIeg4z5z23A'


def test_channel_subscribers(channel):
    """Test for the subscribers property of the Channel class."""
    assert isinstance(channel.subscribers, int) is True


def test_channel_video_count(channel):
    """Test for the video_count property of the Channel class."""
    assert isinstance(channel.video_count, int) is True


def test_channel_views(channel):
    """Test for the views property of the Channel class."""
    assert isinstance(channel.views, int) is True


def test_to_json(channel):
    """Test the to_json method of the Channel class."""
    channel.to_json('channel.json')
    assert os.path.exists('channel.json')

    os.remove('channel.json')
    assert not os.path.exists('channel.json')


def test_print_info(channel):
    """Test the print_info method of the Channel class."""
    with patch('src.channel.Channel._printj') as mock_print:
        channel.print_info()

        mock_print.assert_called_once_with(
            channel._channel_info  # pylint: disable=W0212
        )


def test_get_service():
    """Test the get_service method of the Channel class."""
    service = Channel.get_service()
    assert service is not None


def test_to_int():
    """Test the _to_int method of the Channel class."""
    assert Channel._to_int('1000') == 1000  # pylint: disable=W0212
    assert Channel._to_int('10.5') == 10  # pylint: disable=W0212
    assert Channel._to_int('1.99') == 1  # pylint: disable=W0212


def test_repr(channel):
    """Test the __repr__ method of the Channel class."""
    assert repr(channel) == 'UC-OVMPlMA3-YCIeg4z5z23A'
