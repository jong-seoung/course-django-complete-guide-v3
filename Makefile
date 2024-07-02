run:
	python manage.py runserver

makemigrations:
	python manage.py makemigrations $(app)

migrate:
	python manage.py migrate $(app)

sqlmigrate:
	python manage.py sqlmigrate $(app) $(file)

shell_plus:
	python manage.py shell_plus --print-sql --quiet-load