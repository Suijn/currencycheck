.PHONY: unit check_style reformat

unit:
	poetry run pytest .

check_style:
	poetry run black --check .
	poetry run isort --check .
	poetry run flake8 .

reformat:
	poetry run black .
	poetry run isort .