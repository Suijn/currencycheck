.PHONY: unit check_style reformat

unit:
	poetry run pytest --ignore tests/integration

integration:
	poetry run pytest tests/integration

check_style:
	poetry run black --check .
	poetry run isort --check .
	poetry run flake8 .

reformat:
	poetry run black .
	poetry run isort .