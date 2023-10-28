import os
def get_api_key() -> str:
    """Возвращает API-ключ из переменных окружения."""
    env_var = os.environ
    env_var['YT_API_KEY'] = 'AIzaSyB1z7KSI8FjqZqYXqTWN2424WwijUQrzIs'
    return os.getenv('YT_API_KEY', 'API_KEY_NOT_FOUND')