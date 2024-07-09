# include `.env` file if exists
ifneq ("$(wildcard .env)","")
	include .env
	export
endif

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

# Tests, linters & formatters
fmt:
	make -k ruff-fmt black

lint:
	make -k ruff check black-check mypy

black:
	python -m black ./api

black-check:
	python -m black --check ./api

ruff:
	python -m ruff check ./api

ruff-fmt:
	python -m ruff check --fix-only --unsafe-fixes ./api

test:
	python manage.py test

test.app:
	python manage.py test api.$(app)

test.coverage:
	pytest --cov=template ./api

mypy:
	python -m mypy ./api