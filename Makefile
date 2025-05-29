init:
	docker compose up -d --build

backend-up:
	docker compose exec backend python manage.py runserver 0.0.0.0:8000
frontend-up:
	docker compose exec frontend npm run dev

migrate:
	docker compose exec backend python manage.py migrate

backend-shell:
	docker compose exec backend /bin/bash
frontend-shell:
	docker compose exec frontend /bin/bash

generate-secretkey:
	docker compose exec backend python generate_secretkey.py

makemigrations:
	docker compose exec backend python manage.py makemigrations

flushdata:
	docker compose exec backend python manage.py flush --no-input

createsuperuser:
	docker compose exec backend python manage.py createsuperuser

stop:
	docker compose stop

destroy:
	docker compose down --rmi all --volumes --remove-orphans