from src.channel import Channel


def test_print_info():
    # Создайте экземпляр класса Channel с тестовым channel_id (замените его на реальный)
    list = []
    channel_id = 'UCX44TgNXmA_XcBEaeft2elA'
    channel = Channel(channel_id)
    # Вызовите метод print_info()
    channel.print_info()
    list.append(channel)
    assert len(list) == 1

    # Добавьте здесь утверждения (assert) для проверки ожидаемых результатов
    # Например, проверьте, что информация о канале успешно получена
    # assert len(channel) == 7
