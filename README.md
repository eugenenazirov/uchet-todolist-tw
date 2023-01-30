# Todo-list Backend App TestWork
## Made for Uchet.kz


Tech stack:
- Python 3.10
- Django 3.2.16 LTS
- Djoser 3.14.0
- Celery 5.2.7
- PostgreSQL 15.1
- RabbitMQ 3

### How to run project on your local machine

You should run all following commands from project root directory.
1. Set up your .env file, you can use .env.example to create your own.
Remember to set up your own Postgres account credentials.
2. Activate the virtual environment.
If you have python-venv module, you can create venv by running ```make create-venv```
3. Install dependencies: ```make install-dependencies```
4. If you have your own Postgres and RabbitMQ, set it up first. If not, use docker images with complete infrastructure:
```make run-infra-linux``` or ```make run-infra-macos``` depends on your OS.
If you're on Windows, write your own command to run ./infra/docker-compose.yml
5. Apply migrations: ```make apply migrations```
6. If you want to test email sending on local test SMTP server, run: ```make email-check``` 
7. Run Celery: ```make run-celery```
8. Run Django development server: ```make start```

Enjoy the app!


Test work terms of reference: https://gist.github.com/eugenenazirov/e1a7860eca11a0b0a7ecb4e0fbd8715a