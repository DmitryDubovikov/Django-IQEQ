# Django-IQEQ

## Тестовое задание TeamUp python backend developer

Бизнес требования:
Для тестируемых существуют специальные секретные ключи по которым можно пройти 2 теста. Один из них это IQ второй EQ. В конце тестирования можно посмотреть свои результаты.

## Как запустить

Сбилдить образ:
```
docker build -t iqeq .
```

Запустить контейнер (на windows вместо $(pwd) может потребоваться указать полный путь явно):
```
docker run --name iqeq -p 8000:8000 -v $(pwd):/app iqeq
```
Подключиться к контейнеру:
```
docker exec -it iqeq bash
```
Применить миграции:
```
python manage.py migrate
```

## Как тестировать

С помощью коллекции Postman IQEQ.postman_collection.json: сначала создать логин, потом в остальных ручках указывать созданный логин.

Либо вручную. Адреса ручек:

http://127.0.0.1:8000/api/create-test/

http://127.0.0.1:8000/api/save-iq/

http://127.0.0.1:8000/api/save-eq/

http://127.0.0.1:8000/api/results/
