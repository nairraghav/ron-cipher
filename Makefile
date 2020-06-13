APP_NAME=ciphers

clean:
	rm -rf .pytest_cache/ .coverage build/ dist/ ron_cipher*/ junit_test_report.xml

test:
	python -s -m pytest tests/ --cov=$(APP_NAME)/ --cov-report term-missing --junitxml=junit_test_report.xml

flake:
	flake8 $(APP_NAME)/ tests/

format:
	black $(APP_NAME) --line-length 79

build:
	python setup.py sdist bdist_wheel

local-test:
	pip uninstall -y ron-cipher-nairraghav
	make clean
	make build
	pip install dist/ron_cipher_nairraghav-*-py3-none-any.whl
