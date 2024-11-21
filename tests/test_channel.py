from src.channel import Channel

channel = Channel('UC-OVMPlMA3-YCIeg4z5z23A')

assert channel.channel_id == 'UC-OVMPlMA3-YCIeg4z5z23A'

def test_print_info():
    assert channel.print_info() == None


def test_to_json():
    assert channel.to_json('moscowpython.json') == None