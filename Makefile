install:
	poetry install

test:
	poetry run pytest -vv

test-coverage:
	poetry run pytest --cov=gendifff --cov-report xml

lint:
	poetry run flake8 gendifff

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

.PHONY: install test lint selfcheck check build
