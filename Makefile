.PHONY: unit check_style reformat

unit:
	poetry run pytest --ignore src/tests/integration

integration:
	poetry run pytest src/tests/integration

check_style:
	poetry run black --check .
	poetry run isort --check .
	poetry run flake8 .

reformat:
	poetry run black .
	poetry run isort .