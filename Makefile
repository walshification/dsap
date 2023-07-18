PIPENV_RUN := pipenv run

.PHONY = test fmt deps

test:
	$(PIPENV_RUN) pytest

lint:
	$(PIPENV_RUN) black . --check
	$(PIPENV_RUN) mypy .

fmt:
	$(PIPENV_RUN) black .

shell:
	$(PIPENV_RUN) ipython

deps:
	pipenv install --dev
