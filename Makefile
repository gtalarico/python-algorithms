.PHONY: run db test ci lint clean bash logs stop build test_services circleci

# Colors
NC=\x1b[0m
L_GREEN=\x1b[32;01m

## usage: print useful commands
usage:
	@echo "$(L_GREEN)Choose a command: $(PWD) $(NC)"
	@bash -c "sed -ne 's/^##//p' ./Makefile | column -t -s ':' |  sed -e 's/^/ /'"

## init: Setup Dev Enviromenment
install:
	./scripts/deps.sh
	git config core.hooksPath ./githooks

## rebuild: Rebuild Compose Containers
rebuild:
	docker-compose up -d --force-recreate --build

## start: Start Dev Server
start:
	docker network create apidocs-network; docker-compose up -d web

## restart: Restart docker-compose
restart: stop start

## stop: Stop Dev Server
stop:
	docker-compose down

## logs: Show STDOUT
logs:
	docker-compose logs -f --tail=500

## bash: Show Server STDOUT
bash:
	docker exec -it django bash

## attach: Attach to django server for debugging
attach:
	docker attach django

# deploy: Deploy to heroku
deploy:
	docker build . -f Dockerfile.web -t django-heroku
	heroku container:login
	heroku container:push web --recursive --app apidocs-api
	heroku container:release web --app apidocs-api

## test: run tests
test:
	docker-compose run --rm web python -m pytest

## ci: Circle CI runner
ci:
	circleci local execute

## lint: Flake8
lint:
	docker-compose run --rm --no-deps web flake8 .

## format: Run Black Formatter
format:
	docker-compose run --rm --no-deps web black --exclude=venv\|migrations .

## clean: delete python artifacts
clean:
	python3 -c "import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.py[co]')]"
	python3 -c "import pathlib; [p.rmdir() for p in pathlib.Path('.').rglob('__pycache__')]"

