all: build down migrate collectstatic up

pull:
	docker-compose pull

push:
	docker-compose push

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

# $a [app]
# $n [migrations number]
migrate:
	docker-compose run app bash -c 'python manage.py migrate $(if $a, $a $(if $n, $n,),)'

createsuperuser:
	docker-compose run app bash -c 'python manage.py createsuperuser'

collectstatic:
	docker-compose run app bash -c 'python manage.py collectstatic --no-input'

makemigrations:
	docker-compose run --volume=${PWD}/src:/src app bash -c 'python manage.py makemigrations'
	sudo chown -R ${USER} ./

showmigrations:
	docker-compose run --volume=${PWD}/src:/src app bash -c 'python manage.py showmigrations'

psql:
	docker exec -it user_notes_db psql -U postgres

dev:
	docker-compose run --volume=${PWD}/src:/src --publish=8000:8000 app bash -c 'python manage.py runserver 0.0.0.0:8000'

test:
	docker-compose run app pytest

# $m [marks]
# $k [keyword expressions]
# $o [other params in pytest notation]
dev_test:
	docker-compose run --volume=${PWD}/src:/src app pytest $(if $m, -m $m)  $(if $k, -k $k) $o

command:
	docker-compose run --volume=${PWD}/src:/src app python manage.py ${c}

shell:
	docker-compose run app python manage.py shell

dotenv:
	docker build -t commands ./commands
	docker run commands /bin/sh -c 'python generate_dotenv.py && cat generate_dotenv/.env.example' > $(if $f,$f,.env.tmp)

# $f [dot-env file name]
poetry_lock:
	docker-compose run --rm --no-deps --volume=${PWD}:${PWD} --workdir=${PWD} app poetry lock --no-update
	sudo chown -R ${USER} ./poetry.lock

poetry_add:
	docker-compose run --rm --no-deps --volume=${PWD}:${PWD} --workdir=${PWD} app poetry add $n
	sudo chown -R ${USER} ./poetry.lock ./pyproject.toml

pre-commit-install:
	pip3 install pre-commit
	pre-commit install
	pre-commit install --hook-type commit-msg

lint:
	pre-commit run --all-files

.PHONY: all build up down migrate createsuperuser collectstatic makemigrations psql dev dev_test command shell test debug dotenv piplock pre-commit-install

