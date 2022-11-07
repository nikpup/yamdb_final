## YaMDb Service

The YaMDb project collects user reviews of works. 
The works are divided into categories: "Books", "Films", "Music". 
The list of categories can be expanded by the administrator.


## Technologies

- Django rest_framework
- Django rest_framework_simplejwt
- Django django_filters
- Docker
- Git

## Workflow status

![workflow status](https://github.com/nikpup/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## How to launch a project:

Clone the repository and go to it on the command line:
```sh
git clone ...
```


Create .env file in infra directory and fill it like this:

```sh
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin
DB_HOST=db
DB_PORT=5432
```

Launch api in containers:

```sh
cd /infra
docker-compose up -d --build
```

Perform migrations and collect statics:

```sh
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py collectstatic --no-input 
```

Fill the database with data in infra/fixtures.json:

```sh
docker-compose exec web python manage.py loaddata fixtures.json 
```
The image of api is available on [DockerHub](https://hub.docker.com/repository/docker/peterzzz98/api-yamdb).

The project is available at http://84.201.152.100/