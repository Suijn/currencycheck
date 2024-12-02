.PHONY: server unit integration down check_style reformat

server:
	docker compose up --build server

unit:
	poetry run pytest --ignore tests/integration

integration:
	docker compose up --build integration_tests

down:
	docker compose down -v

check_style:
	poetry run black --check .
	poetry run isort --check .
	poetry run flake8 .

reformat:
	poetry run black .
	poetry run isort .