from src.channel import Channel

if __name__ == '__main__':
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')

    print(moscowpython.title)
    print(moscowpython.videoCount)
    print(moscowpython.url)

    moscowpython.channel_id = 'Новый ID канала' # здесь должен быть правильный ID канала на YouTube
    print(Channel.get_service())

    moscowpython.to_json('moscowpython.json')
