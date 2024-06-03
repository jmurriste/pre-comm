pip install black pylint flake8 radon ruff isort
black --config .black.toml .
pylint *.py
flake8 --config .flake8
mypy .
ruff check .
isort . --settings .isort.cfg