.PHONY: dev test deploy migrate

dev:
	docker-compose up

migrate:
	docker-compose exec api bash /app/scripts/migrate.sh

deploy:
	bash scripts/deploy.sh