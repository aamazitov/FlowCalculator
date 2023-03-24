#Создание БД
### 1. Скачать СУБД PostgreSQL версии 15.2 под винду https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
### 2. Установить, задав логин/пароль: postgres/postgres
### 3. Создать базу flowcalcdb

#Перед первым запуском:
### 1. python -m venv venv
### 2. venv\scripts\activate
### 3. pip install -r requirements.txt
### 4. flask db init
### 5. flask db migrate -m "tables"
### 6. flask upgrade
### 7. flask run

#Для обновления структуры БД:
### 1. flask db migrate -m "tables"
### 2. flask upgrade