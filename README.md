# Проект Foodgram

![Github actions](https://github.com/methodologyCode/foodgram-project-react/actions/workflows/main.yml/badge.svg)


### Как запустить проект локально в контейнерах:

Клонировать репозиторий и перейти в него из командной строки:

``` git@github.com:methodologyCode/foodgram-project-react.git ``` 
``` cd foodgram-project-react ``` 

Запустить docker-compose:

```
docker-compose up

```

После окончания сборки контейнеров выполнить миграции:

```
docker-compose exec web python manage.py migrate

```

Создать суперпользователя:

```
docker-compose exec web python manage.py createsuperuser

```

Загрузить статику:

```
docker-compose exec web python manage.py collectstatic --no-input 

```

Проверить работу проекта по ссылке:

```
http://localhost/api/
```


### Как запустить проект локально:

Создать и активировать виртуальное окружение:

``` python3 -m venv venv ``` 

#### Linux/macOS:
``` source venv/bin/activate ```  
``` python3 -m pip install --upgrade pip ``` 

Установить зависимости из файла requirements.txt:

``` pip install -r requirements.txt ``` 

Выполнить миграции:

``` python3 manage.py migrate ``` 

Запустить проект:

``` python3 manage.py runserver ``` 

### В API доступна документация

``` http://localhost/redoc ```



