import os
import requests


class Channel:
    def __init__(self, channel_id):
        self.channel_id = channel_id

    def print_info(self):
        api_key = "AIzaSyCWPxoY0OGIHIFtENq5bkq58n5DzlRU-l8"
        # api_key = os.environ.get("YouTube_API")

        if not api_key:
            print("API не найден.")
            return

        # Формируем URL к YouTube API
        url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={self.channel_id}&key={api_key}"

        try:
            # Отправляем GET-запрос к YouTube API
            response = requests.get(url)
            response.raise_for_status()  # Проверяем статус ответа

            # Получаем данные из ответа в формате JSON
            channel_data = response.json()

            # Извлекаем необходимую информацию из ответа
            snippet = channel_data.get("items", [{}])[0].get("snippet", {})
            statistics = channel_data.get("items", [{}])[0].get("statistics", {})

            # Вывод информации о канале
            print("Title:", snippet.get("title", "N/A"))
            print("Description:", snippet.get("description", "N/A"))
            print("Subscriber Count:", statistics.get("subscriberCount", "N/A"))
            print("View Count:", statistics.get("viewCount", "N/A"))
            print("Video Count:", statistics.get("videoCount", "N/A"))

        except requests.exceptions.HTTPError as errh:
            print("HTTP Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print("Something went wrong:", err)


if __name__ == '__main__':
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    moscowpython.print_info()
