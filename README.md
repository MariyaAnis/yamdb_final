### Описание проекта api_final_yatube:

api_yamdb - групповой учебный проект 10-го спринта курса backend-разработки
Яндекс.Практикума

![example workflow](https://github.com/MariyaAnis/yamdb_final/actions/workflows/yamdb_workflow.ymlbadge.svg)

### Как запустить проект:

Склонируйте репозитрий на свой компьютер
Создайте .env файл в директории infra/, в котором должны содержаться следующие переменные:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME= # название БД\ POSTGRES_USER= # ваше имя пользователя
POSTGRES_PASSWORD= # пароль для доступа к БД
DB_HOST=db
DB_PORT=5432\
```
Из папки infra/ соберите образ при помощи docker-compose 
```
$ docker-compose up -d --build
```
Примените миграции 
```
$ docker-compose exec web python manage.py migrate
```
Соберите статику 
```
$ docker-compose exec web python manage.py collectstatic --no-input
``` 
Для доступа к админке создать суперюзера 

```
$ docker-compose exec web python manage.py createsuperuser
```


### Документация:

Примеры обращений к эндпоинтам находятся по адресу:

```
http://127.0.0.1:8000/redoc/
```