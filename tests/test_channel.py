""" Channel test module """

import json
from unittest import mock

from src.channel import Channel


def test_channel_print_info(mock_youtube):
    """
    Test the print_info method of the Channel class.

    It ensures that the method retrieves channel information using
    the YouTube API and prints the information in the expected format.
    """
    channel = Channel(channel_id='your_channel_id')
    channel.youtube = mock_youtube

    mock_channels_list = mock_youtube.channels().list().execute
    mock_channels_list.return_value = {
        'items': [
            {
                'id': 'your_channel_id',
                'snippet': {
                    'title': 'Your Channel Name',
                    'description': 'Your Channel Description'
                },
                'statistics': {
                    'viewCount': '1000',
                    'subscriberCount': '500',
                    'videoCount': '10'
                }
            }
        ]
    }

    with mock.patch('builtins.print') as mock_print:
        channel.print_info()

        expected_output = {
            'items': [
                {
                    'id': 'your_channel_id',
                    'snippet': {
                        'title': 'Your Channel Name',
                        'description': 'Your Channel Description'
                    },
                    'statistics': {
                        'viewCount': '1000',
                        'subscriberCount': '500',
                        'videoCount': '10'
                    }
                }
            ]
        }

        mock_print.assert_called_once_with(
            json.dumps(
                expected_output,
                indent=2,
                ensure_ascii=False
            )
        )


def test_channel_get_channel_id_by_channel_name(mock_youtube):
    """
    Test the _get_channel_id_by_channel_name method of the Channel class.

    It ensures that the method retrieves the channel ID by channel name
    using the YouTube API and returns the correct channel ID.
    """
    channel = Channel(channel_name='Your Channel Name')
    channel.youtube = mock_youtube

    mock_search_list = mock_youtube.search().list().execute
    mock_search_list.return_value = {
        'items': [
            {
                'id': {
                    'channelId': 'your_channel_id'
                }
            }
        ]
    }

    channel_id = channel._get_channel_id_by_channel_name() # pylint: disable=W0212

    assert channel_id == 'your_channel_id'
