# Парсер
## Инструкция запуска 
```Docker
sudo apt install redis # скачиваем redis
cd workdir/doramy_top/ # вход в рабочую директорию
virtualenv venv # создание переменного окружения
source venv/bin/activate # активация переменного окружения
pip install -r requirements.txt # установка библиотек
cd src/ # вход в папку с Django-проектом
python3 manage.py runserver # запуск проекта
celery -A config worker -l info # запуск Celery
```

`workdir` - путь до проекта