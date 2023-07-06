PIPENV_RUN := pipenv run

.PHONY = test fmt deps

test:
	$(PIPENV_RUN) black . --check
	$(PIPENV_RUN) mypy .
	$(PIPENV_RUN) pytest

fmt:
	$(PIPENV_RUN) black .

deps:
	pipenv install --dev
