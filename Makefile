# Makefile

install:
	pip install -r requirements.txt

quickstart:
	python quickstart.py

test:
	pytest tests/