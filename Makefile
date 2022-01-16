test:
	black . --check
	mypy .
	pytest

fmt:
	black .
