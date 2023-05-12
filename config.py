from environs import Env
import os


def load_secret_key():
    path = os.path.join(os.path.dirname(__file__), '.env')
    env = Env()  # Создаем экземпляр класса Env
    env.read_env(path)  # Методом read_env() читаем файл .env и загружаем из него переменные в окружение
    secret_key = env('SECRET_KEY')  # Сохраняем значение переменной окружения в переменную secret_key

    return secret_key
