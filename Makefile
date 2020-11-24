ci: lint
	@tox -p

clean:
	@rm -rf build/ dist/

help:
	@echo
	@echo "  make ci          Run continuous integration checks locally."
	@echo "  make clean       Clean up after making a package."
	@echo "  make help        Show this help."
	@echo "  make init        Install development dependencies."
	@echo "  make install     Install Elemental in editable mode."
	@echo "  make lint        Lint the code."
	@echo "  make package     Build the package."
	@echo "  make push        Push the main branch to the repo."
	@echo "  make release     Release to PyPI."
	@echo "  make tag         Make the Git tag for the release."
	@echo "  make test        Run the tests in the development environment."

init:
	@pip install -r requirements.txt

install:
	@pip install -e .

lint:
	@echo "Running Flake8"
	@flake8
	@echo "Running isort"
	@isort **/*.py -c
	@echo "Running pydocstyle"
	@pydocstyle
	@echo "Running Pylint"
	@pylint *.py
	@pylint elemental/.
	@pylint \
		--disable=duplicate-code \
		--disable=missing-class-docstring \
		--disable=missing-function-docstring \
		--disable=no-self-use \
		--disable=too-few-public-methods \
		tests/.
	@echo "Running twine check"
	@python setup.py sdist > /dev/null
	@twine check dist/*
	@rm -rf build/ dist/ elemental.egg-info/

package:
	@python setup.py sdist bdist_wheel

publish:
	@twine upload dist/*

push:
	@git checkout main
	@git push origin main
	@git push origin v`python setup.py --version`

release:
	@git add CHANGELOG.rst docs/source/conf.py elemental/__init__.py
	@git commit -m "Release v`python setup.py --version`"
	@git tag \
		-a v`python setup.py --version` \
		-m "Elemental v`python setup.py --version`"

test:
	@pytest --cov=elemental --cov-report=term-missing tests/

.DEFAULT_GOAL:= help
