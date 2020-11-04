init:
	@if [ ! -d "./venv" ]; then python3 -m venv venv; fi
	@echo "Use following commands:"
	@echo
	@echo "To activate   - . venv/bin/activate"
	@echo "To deactivate - deactivate"
	@echo

setup:
	@pip install -U pip
	@pip install -r requirements.txt

upgrade:
	@pip install -Ur req_list.txt
	@pip freeze > requirements.txt

newapp:
ifdef APP
	@python manage.py startapp $(APP)
else
	@echo "APP variable not found"
endif

static:
	@python manage.py collectstatic -c --noinput

super:
	@python manage.py createsuperuser --username admin --email ''

clean:
	@find . -path ./venv -prune -o \( \
		-name "*.pyc" -o \
		-name "__pycache__" -o \
		-name ".DS_Store" -o \
		-name "Thumb.db" \)  -exec rm -rf {} +

reset: clean
	@rm -rf db.sqlite3 ./venv

check:
	@python manage.py check

migrate: check
	@python manage.py makemigrations
	@python manage.py migrate

run: migrate
	@python manage.py runserver 0.0.0.0:8000

test:
	@python manage.py test

.PHONY: init setup clean check migrate run static super newapp upgrade