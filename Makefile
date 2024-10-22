install:
	@echo "Installing requirements..."
	pip install -r requirements.txt

migrate:
	@echo "Running migrations..."
	python manage.py migrate

start: migrate
	@echo "Starting server..."
	python manage.py runserver
