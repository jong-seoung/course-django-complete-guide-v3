.SHELLFLAGS = -ec

ENV_PATH=/srv/config/django.env
PYTHON=/srv/venv/bin/python
MANAGE=ENV_PATH=$(ENV_PATH) $(PYTHON) manage.py

pull:
	git pull

createsuperuser:
	$(MANAGE) createsuperuser

collectstatic:
	$(MANAGE) collectstatic --no-input

shell:
	$(MANAGE) shell

showmigrations:
	$(MANAGE) showmigrations

migrate:
	$(MANAGE) migrate

createsuperuser:
	$(MANAGE) createsuperuser

log:
	journalctl -u django --since "1 hour ago" -f
	
restart:
	sudo systemctl restart django.service
	
nginx-edit:
	sudo nano /etc/nginx/sites-available/default

nginx-edit-vim:
	sudo vim /etc/nginx/sites-available/default

nginx-reload:
	sudo systemctl reload nginx
	
nginx-restart:
	sudo systemctl restart nginx
