setup:
	pip install pipenv
	pipenv install

clean:
	find . -name '.pytest_cache' -exec rm -fr {} +
	find . -name '.coverage' -exec rm -fr {} +
	find . -name '.coverage.*' -exec rm -fr {} +
	find . -name '.mypy_cache' -exec rm -fr {} +

tests:
	pipenv run pytest --cov=. --cov-fail-under 100

checks: clean tests
	pipenv run mypy --strict weather/ 
	pipenv run mypy --strict test/ 