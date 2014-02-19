develop: setup-git
	pip install "file://`pwd`#egg=mobileapps_store[dev]"
	pip install -e .

setup-git:
	git config branch.autosetuprebase always
	cd .git/hooks && ln -sf ../../hooks/* ./

lint-python:
	@echo "Linting Python files"
	PYFLAKES_NODOCTEST=1 flake8 mobileapps_store
	@echo ""
