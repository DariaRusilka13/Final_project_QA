-- Задание 1: логины курьеров и количество заказов в доставке

SELECT c.login, 
		COUNT(*) AS orders_in_delivery 
FROM "Couriers" AS c 
JOIN "Orders" AS o ON c.id = o."courierId" 
WHERE o."inDelivery" = true 
GROUP BY c.login;

-- Задание 2: трекеры заказов и их статусы

SELECT track,
              finished,
              cancelled,
              "inDelivery",
       CASE
           WHEN finished = true THEN 2
           WHEN cancelled = true THEN -1
           WHEN "inDelivery" = true THEN 1
           ELSE 0
       END AS status
FROM "Orders"
ORDER BY track;