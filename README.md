# E9

Необходимо установить docker и docker-compose.
Собрать образы командой
```
    docker-compose build
```
Их запустить с помощью команды 
```
    docker-compose up
```
Открыть ссылку
```
    http://0.0.0.0:5000/ 
```
Должно заработать...
Но...все очень сырое и куча ошибок.
Хотелось все попробовать в блоке и на отладку времени не хватило(((
```
export FLASK_APP=api/app
export FLASK_ENV=development

alembic init alembic
alembic revision --autogenerate -m "initial migration"
alembic upgrade head


```