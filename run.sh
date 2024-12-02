#!/bin/bash

if [ "$1" = "server" ]; then
  echo Running server

  /app/.venv/bin/poetry run streamlit run src/currencycheck/entrypoints/streamlit_server.py
elif [ "$1" = "integration_test" ]; then
  echo Runnig integration_tests
  .venv/bin/poetry run pytest tests/integration
fi