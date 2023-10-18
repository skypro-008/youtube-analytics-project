import pytest

from src.channel import Channel


@pytest.fixture
def make_channel():
    return Channel("AIzaSyB1z7KSI8FjqZqYXqTWN2424WwijUQrzIs")


def test_class(make_channel):
    channel = make_channel
    assert isinstance(channel, object)


def test_init(make_channel):
    channel = make_channel
    assert channel.id == "AIzaSyB1z7KSI8FjqZqYXqTWN2424WwijUQrzIs"