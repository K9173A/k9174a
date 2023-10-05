# Development targets
dev.up:
	docker compose -f docker-compose.prod.yml -f docker-compose.dev.yml --env-file .env.dev up
dev.build:
	docker-compose -f docker-compose.prod.yml -f docker-compose.dev.yml --env-file .env.dev build
dev.exec.app.bash:
	docker-compose -f docker-compose.prod.yml -f docker-compose.dev.yml exec app bash
dev.exec.app.make:
	docker-compose -f docker-compose.prod.yml -f docker-compose.dev.yml exec app bash -c 'make $(command)'
dev.exec.app.migrate:
	$(MAKE) dev.exec.app.make command=makemigrations
	$(MAKE) dev.exec.app.make command=migrate

# Documentation targets
docs.up:
	docker compose -f docker-compose.prod.yml -f docker-compose.dev.yml -f docker-compose.docs.yml --env-file .env.dev up
docs.build:
	docker-compose -f docker-compose.prod.yml -f docker-compose.dev.yml -f docker-compose.docs.yml --env-file .env.dev build

# Production targets
prod.up:
	docker compose -f docker-compose.prod.yml up
prod.build:
	docker compose -f docker-compose.prod.yml build

# Miscellaneous targets
stop:
	docker compose stop
down:
	docker compose down --remove-orphans
clean:
	docker compose down --remove-orphans --volumes