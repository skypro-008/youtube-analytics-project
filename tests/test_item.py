from src.channel import Channel


# def test_print_info():
#     list = []
#     channel_id = 'UCX44TgNXmA_XcBEaeft2elA'
#     channel = Channel(channel_id)
#     # Вызовите метод print_info()
#     channel.print_info()
#     list.append(channel)
#     assert len(list) == 1


def test_Channel():
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    assert moscowpython.title == 'MoscowPython'
    assert moscowpython.video_count == 707
    assert moscowpython.url == 'https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A'
