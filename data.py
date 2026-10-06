# заголовки для HTTP-запроса, указывающие на то, что тело запроса будет в формате JSON
headers = {
    "Content-Type": "application/json"
}

# данные для создания нового заказа в системе
order_body = {
    "firstName": "Роман",
    "lastName": "Иванов",
    "address": "Ленина, 12",
    "metroStation": 5,
    "phone": "+79264561661",
    "rentTime": 2,
    "deliveryDate": "2026-12-01",
    "comment": "Не звонить в дверь",
    "color": [
        "BLACK"
    ]
}