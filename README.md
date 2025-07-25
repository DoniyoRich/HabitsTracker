# Домашнее задание 35.2 CI/CD и GitHub Actions

## Деплой Django приложения с Docker, PostgreSQL и GitHub Actions

### IP -  51.250.41.144/swagger/

### Описание проекта
  - Проект "Трекер привычек" автоматизирует процесс тестирования, сборки и деплоя Django приложения с использованием Docker, PostgreSQL и GitHub Actions CI/CD.

### Предварительные требования
#### Для локальной разработки:
 - Docker
 - Python 3.12
 - Учетная запись на Docker Hub

#### Для сервера:
  - Ubuntu сервер (в данном проекте реализован на Yandex Cloud)
  - SSH доступ к серверу
  - Доменное имя (опционально)

### Настройка сервера

#### Установка Docker

```
sudo apt update
sudo apt install -y docker.io
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -aG docker $USER
newgrp docker
```
#### Установка и настройка PostgreSQL
```
sudo apt install -y postgresql postgresql-contrib
sudo systemctl start postgresql
sudo systemctl enable postgresql
```
#### Создание пользователя и БД:

```
sudo -u postgres psql
```

```
CREATE DATABASE yourdbname;
CREATE USER youruser WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE yourdbname TO youruser;
\q
```
#### Настройка доступа:

```
sudo nano /etc/postgresql/14/main/pg_hba.conf
```
#### Добавьте:

```
host    all             all             0.0.0.0/0               md5
```
```
sudo nano /etc/postgresql/14/main/postgresql.conf
```
#### Раскомментируйте:
```
listen_addresses = '*'
```

Перезапуск:

```
sudo systemctl restart postgresql
sudo ufw allow 5432/tcp
```

### Подготовка .env файла
Создайте файл .env в /home/user1/habits/ с содержимым:

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=yourdbname
DB_USER=youruser
DB_PASSWORD=yourpassword
DB_HOST=your-server-ip
DB_PORT=5432
SECRET_KEY=yoursecretkey
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,server_ip
```

### Настройка GitHub Secrets

В настройках репозитория (Settings → Secrets → Actions) добавьте:
```
DOCKER_HUB_USERNAME - ваш логин Docker Hub
DOCKER_HUB_ACCESS_TOKEN - токен Docker Hub
SSH_KEY - приватный SSH ключ
SSH_USER - пользователь сервера (например, user1)
SERVER_IP - IP вашего сервера
```

### Workflow CI/CD

Процесс автоматической сборки и деплоя включает:

```
lint - проверка кода flake8
test - запуск unit-тестов
build - сборка Docker образа
deploy - деплой на сервер
```

#### Workflow запускается при каждом push или pull request.

Docker образ
Конфигурация включает:

  - Оптимизированные переменные Python
  - Установку зависимостей
  - Настройку прав для статических файлов
  - Запуск Gunicorn

### Ручной деплой
Получение образа:

```
docker pull ваш_логин/myapp:тег
```

Миграции:
```
docker run --rm --env-file .env ваш_логин/myapp:тег python manage.py migrate
```

Запуск:

```
docker run -d --name myapp --env-file .env -p 80:8000 ваш_логин/myapp:тег
```

### Доступ к приложению
После деплоя приложение доступно по IP сервера:  51.250.41.144 на порту 80.


[Doniyor Ishanov. ](#) - [SkyPro IT School](#)