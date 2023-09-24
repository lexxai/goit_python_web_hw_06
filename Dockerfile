# Docker-команда FROM вказує базовий образ контейнера
# Наш базовий образ - це Linux з попередньо встановленим python-3.11
FROM python:3.11-slim
# FROM python:3.11

# Встановимо змінну середовища

ENV APP_HOME /app 

# Встановимо робочу директорію всередині контейнера
WORKDIR $APP_HOME

# Скопіюємо інші файли в робочу директорію контейнера
COPY . .

# Встановимо залежності всередині контейнера
# RUN pip install -r requirements.txt 
# RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt
RUN pip install --no-cache -r requirements.txt 


VOLUME $APP_HOME/db


# Запустимо наш застосунок всередині контейнера
ENTRYPOINT [ "python", "hw_06/main.py" ]

