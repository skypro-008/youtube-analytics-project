from src.channel import Channel

if __name__ == '__main__':
    # Создаем два экземпляра класса

    #
    # НАЧАЛО программы
    #

    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    highload = Channel('UCwHL6WHUarjGfUM_586me8w')

    # Используем различные магические методы
    print()
    print(moscowpython)  # 'MoscowPython (https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A)'
    print(highload)  #
    print(f'\n\033[32mКанал {moscowpython.title}\033[39m:\n')
    print(moscowpython.__repr__())
    print(f'\n\033[32mКанал {highload.title}\033[39m:\n')
    print(highload.__repr__())
    print('\n\033[32mКоличество подписчиков у каналов\033[39m:')
    print(f'Канал {moscowpython.title}: \033[32m{moscowpython.subscriber_count}\033[39m')
    print(f'Канал {highload.title}: \033[32m{highload.subscriber_count}\033[39m')
    print()
    print(f'Сумма подписчиков обоих каналов: \033[32m{moscowpython + highload}\033[39m')  #

    # 100100
    print(f'Разность подписчиков канала {moscowpython.title} и {highload.title}:'
          f' \033[32m{moscowpython - highload}\033[39m')  # -48300
    print(f'Разность подписчиков канала {highload.title} и {moscowpython.title}:'
          f' \033[32m{highload - moscowpython}\033[39m')  # 48300
    print('\n\033[32mСравнение количества подписчиков\033[39m')
    print(f'Количество подписчиков канала {moscowpython.title} > количества '
          f'подписчиков канала {highload.title}: '
          f'\033[32m{moscowpython > highload}\033[39m')
    print(f'Количество подписчиков канала {moscowpython.title} >= количества '
          f'подписчиков канала {highload.title}: '
          f'\033[32m{moscowpython >= highload}\033[39m')  # False
    print(f'Количество подписчиков канала {moscowpython.title} < количества '
          f'подписчиков канала {highload.title}: '
          f'\033[32m{moscowpython < highload}\033[39m')  # True
    print(f'Количество подписчиков канала {moscowpython.title} <= количества '
          f'подписчиков канала {highload.title}: '
          f'\033[32m{moscowpython <= highload}\033[39m')  # True
    print(f'Количество подписчиков канала {moscowpython.title} = количества '
          f'подписчиков канала {highload.title}: '
          f'\033[32m{moscowpython == highload}\033[39m')  # False

    #
    # КОНЕЦ программы
    #