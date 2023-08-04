def test_get_info(channel):
    assert channel.get_info()["items"][0]["snippet"]["title"] == "MoscowPython"


def test_attributes(channel):
    assert channel.title == "MoscowPython"
    assert channel.url == "https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A"
    assert channel.channel_id == "UC-OVMPlMA3-YCIeg4z5z23A"
