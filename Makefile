format:
	black lambda_function.py service/
	isort --profile black lambda_function.py service/

lint:
	black --check lambda_function.py service/
	isort --profile black --check lambda_function.py service/
	flake8 lambda_function.py service/
	mypy lambda_function.py service/

test:
	pytest -v --cov --cov-report xml:coverage.xml --cov-report term tests/

deploy:
	sls deploy
