from src.channel import Channel

if __name__ == '__main__':
    #
    # НАЧАЛО программы
    #

    print('\n Чтение данных о ютуб канале: ')
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')

    print(moscowpython)
    print()

    # получаем значения атрибутов
    print(moscowpython.title)  # MoscowPython
    print(moscowpython.video_count)  # 685 (может уже больше)
    print(moscowpython.url)  # https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A

    print('\n Замена данных об ИД канала: ')
    # менять не можем
    print(f'До изменения - {moscowpython.channel_id}')
    temp_id = 'Новое название'
    moscowpython.channel_id = temp_id
    print(f'Меняем на  - {temp_id}')
    print(f'После изменения - {moscowpython.channel_id}')
    # AttributeError: property 'channel_id' of 'Channel' object has no setter

    print('\n Получить объект для работы с API вне класса: ')
    # можем получить объект для работы с API вне класса
    print(Channel.get_service())
    # <googleapiclient.discovery.Resource object at 0x000002B1E54F9750>

    temp_id = 'moscowpython.json'
    print(f'\n Пишем список в файл: {temp_id}')
    # создаем файл 'moscowpython.json' в данными по каналу
    moscowpython.to_json(temp_id)

    #
    # КОНЕЦ программы
    #
