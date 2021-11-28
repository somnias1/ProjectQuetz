# Django: Quetz

Un sistema de foros basado en Django, preparado para el deploy en Heroku y uso de S3 para el alojamiento de imágenes

Esta aplicación es compatible con el artículo [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python)

## Corriendo de manera local

Asegurarse de tener Python 3.9 [instalado localmente](https://docs.python-guide.org/starting/installation/). Para hacer push a Heroku, se hace uso de la [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), así como [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone https://github.com/somnias1/ProjectQuetz.git
$ cd ProjectQuetz

$ python3 -m venv env-Quetz
$ pip install -r requirements.txt

$ createdb quetz

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

La aplicación debería estarse ejecutando en [localhost:5000](http://localhost:5000/).

## Haciendo deploy a Heroku

```sh
$ heroku create
$ git push heroku main

$ heroku run python manage.py migrate
$ heroku open
```
También se puede hacer uso de la guía

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Documentación

Para más información sobre el uso de Python en Heroku, se pueden revisar los artículos en el Dev Center:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
