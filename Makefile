create-venv:
	python3 -m venv ./venv

install-dependencies:
	pip install -r requirements.txt

apply-migrations:
	python ./manage.py migrate todolist
	python ./manage.py migrate

install: install-dependencies apply-migrations

start:
	python ./manage.py runserver

email-check:
	python -m smtpd -n -c DebuggingServer localhost:1025

run-infra-linux:
	sudo docker compose -f ./infra/docker-compose.yml --project-name=todolist up -d

run-infra-macos:
	docker-compose -f ./infra/docker-compose.yml --project-name=todolist up -d

run-celery:
	celery -A todolist worker --loglevel=INFO
