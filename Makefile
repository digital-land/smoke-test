test:
	python -m pytest -p no:warnings tests

init:
	pip install -r requirements.txt
	python -m playwright install chromium
