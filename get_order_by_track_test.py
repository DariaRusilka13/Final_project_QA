# Дарья Русилко, 48-я когорта — Финальный проект. Инженер по тестированию плюс

# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.
import sender_stand_request

# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов.
import data

def test_get_order_by_track_returns_200():
    # Создание нового заказа с использованием данных из модуля data
    create_response = sender_stand_request.post_new_order(data.order_body)
    
    # Проверка, что заказ был успешно создан (код ответа 201)
    assert create_response.status_code == 201
    
    # Извлечение номера заказа из ответа на создание заказа
    track_number = create_response.json().get("track")
    
    # Получение информации о заказе по его номеру
    get_response = sender_stand_request.get_order(track_number)
    
    # Проверка, что информация о заказе была успешно получена (код ответа 200)
    assert get_response.status_code == 200
    
