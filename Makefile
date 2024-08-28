install:
	poetry install

lint:
	poetry run flake8 gendiff_tk

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff_tk --cov-report xml