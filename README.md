Tests Service
---
Техническое задание
---
Нужно сделать простой сервис проведения тестирования по каким-либо темам. 
Т.е. есть тесты с вариантами ответов, один или несколько вариантов должны быть правильными. 
Тесты группируются в наборы тестов, которые затем пользователь может проходить и 
видеть свой результат.

Описание
---
Tests Service - Сервис для создания и прохождения тестов

Функционал
---
- добавления/обновление/удаление тестов
- регистрация/авторизация пользователей
- прохождение тестов с сохранением результата и возможности закончить тест позже
- вывод статистики по пройденным тестам
- добавление/редактирование/удаление тестов


Системные требования
---
- Windows / Linux / MacOS
- Docker
- Docker-compose

Стек 
---
- Python
- Django
- PostgreSQL
- Nginx
- gunicorn
- Docker, docker-compose

Зависимости
---
- Django==4.1.3
- djangorestframework==3.14.0  
- psycopg2=2.9.5
- gunicorn==20.1.0


Запуск проекта
---
1.  Клонировать проект и перейти в его корень:

		git clone https://github.com/Kolobok99/tests_service
		cd tests_service

2. Создать директорию с .env.prod. файлами
		
	    cd backend
		mkdir .env.prod
		cd .env.prod

3. Инициализировать .env.settings со следующими переменными:

	    DEBUG=0
		SECRET_KEY={your_secret_key}
		DJANGO_ALLOWED_HOSTS={your_host_ip}

        POSTGRES_NAME=tests_db
	    POSTGRES_USER=manager
	    POSTGRES_PASSWORD={your_sql_password}
	    POSTGRES_HOST=db
	    POSTGRES_PORT={your_sql_port}
		
        API_HOST={your_host_ip_with_port}
		STRIPE_PUBLISH_API_KEY={your_stripe_publish_api_key}
		STRIPE_SECRET_API_KEY={your_stripe_secret_api_key}
        
		DATABASE=postgres

4. Инициализировать .env.prod.db со следующими переменными:

		POSTGRES_DB=tests_db
		POSTGRES_USER=manager
		POSTGRES_PORT={your_sql_port}
		POSTGRES_PASSWORD={your_sql_password}

5. Собрать проект

		cd ../docker-composes
		docker compose -f docker-compose.prod.yml build

6. Запустить проект

		docker compose -f docker-compose.prod.yml up

