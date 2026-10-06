# Импортируем модуль configuration - он содержит настройки подключения 
import configuration

# Импортируем модуль requests, который предназначен для отправки HTTP-запросов
import requests

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data 

# 1. Функция создания заказа
def post_new_order(body):
    # Отправка POST-запроса на создание нового заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH, 
                         headers=data.headers, json=body)

# 2. Функция получения заказа по его номеру
def get_order(track_number):
    # Отправка GET-запроса на получение информации о заказе
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDERS_PATH + str(track_number))