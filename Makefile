.PHONY = test fmt deps

test:
	black . --check
	mypy .
	pytest

fmt:
	black .

deps:
	pipenv install --dev
