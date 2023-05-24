""" Conftest module """

from unittest import mock

import pytest


@pytest.fixture
def mock_youtube():
    """
    Fixture for mocking the YouTube API build function.

    It patches the 'src.channel.build' function and returns the mock
    build object.
    """
    with mock.patch('src.channel.build') as mock_build:
        yield mock_build.return_value
