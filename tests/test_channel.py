from src.channel import Channel


def test_get_info():
    channel = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    assert channel.get_info()["items"][0]["snippet"]["title"] == "MoscowPython"
