ROOT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
TARGET_PYTHON_VERSION := python3
VENV_DIR := $(ROOT_DIR)/.venv
REQUIREMENTS_DIR := $(ROOT_DIR)/requirements
VENV_PIP := $(VENV_DIR)/bin/pip
VENV_PYTHON := $(VENV_DIR)/bin/python
MANAGE_FILE := $(ROOT_DIR)/k9174a/manage.py

# Environment targets
venv.create:
	$(TARGET_PYTHON_VERSION) -m venv $(VENV_DIR)
venv.install:
	$(VENV_PIP) install -r $(REQUIREMENTS_DIR)/requirements-$(mode).txt
venv.clean:
	rm -rf $(VENV_DIR)

# Django targets
runserver: ## Запуск сервера
	$(VENV_PYTHON) $(MANAGE_FILE) runserver 0.0.0.0:7777
makemigrations: ## Создание миграций
	$(VENV_PYTHON) $(MANAGE_FILE) makemigrations
migrate: ## Применение миграций
	$(VENV_PYTHON) $(MANAGE_FILE) migrate
test: ## Тестирование приложений
	$(VENV_PYTHON) $(MANAGE_FILE) test k9174a
startapp:
	$(VENV_PYTHON) $(MANAGE_FILE) startapp $(app)