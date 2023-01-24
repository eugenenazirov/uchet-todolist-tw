install-dependencies:
	pip install -r requirements.txt

install-migrations:
	python ./manage.py migrate todolist
	python ./manage.py migrate

install: install-dependencies install-migrations

start:
	python ./manage.py runserver

email-check:
	python -m smtpd -n -c DebuggingServer localhost:1025
