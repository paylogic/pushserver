SHELL := /bin/bash
PATH := $(PWD)/env/bin:$(PATH)
python_version := 2.6
cov_report := html
pip_args :=

.PHONY: test clean

env:
ifndef local_env
	PATH=/usr/bin/:/usr/local/bin virtualenv env --no-site-packages -p python$(python_version)
	env/bin/pip install -U setuptools $(pip_args)
	env/bin/pip install -U pip $(pip_args)
endif

develop: env
	pip install -r requirements.txt $(pip_args)

clean:
	-rm -rf ./build

build:
	pip install -r requirements.txt --target=./build
	cp -R pushserver *.py ./build/

dependencies:
	sudo apt-get install `cat DEPENDENCIES* | grep -v '#'`
