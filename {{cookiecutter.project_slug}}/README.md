# backend-muvien
Backend da Muvien
# Project Setup

## Prerequisites
- Python
- Poetry
- Docker
- Docker Compose

## Enable Poetry's Virtual Environment
```
poetry shell
```

## Install Dependencies
```
poetry install
```

## Apply Migrations
```
poetry run python manage.py migrate
```

## To format code
```
make fmt
```

## To lint code
```
make lint
```

## To run tests on all apps
```
make test
```

## To run tests on a specific app
```
make test app=<app_name>
```

