For basic settup see notes on quick-todo

## Django Rest Framework (DRF)

Used to build RESTful APIs with Django.

DRF is composed of the following components:

1. Serializers are used to convert Django QuerySets and model instances to (serialization) and from (deserialization) JSON (and a number of other data rendering formats like XML and YAML).
2. Views (along with ViewSets), which are similar to traditional Django views, handle RESTful HTTP requests and responses. The view itself uses serializers to validate incoming payloads and contains the necessary logic to return the response. Viewsets are coupled with routers, which map the views back to the exposed URLs.

Note:

1. In order to work with image blobs, install:
   `pip install Pillow`

Installing django rest framework:
`pip3 install djangorestframework markdown django-filter`

## Create App

1. `python manage.py startapp <appName>`
2. register app in `settings.py` by adding it to `INSTALLED` list

## Using Postgres

1. Run `pip install psycopg2`
2. Update database variable in `settings.py`

## Create database tables

1. Add models to the apps' `models.py` files
2. run `python manage.py makemigrations`
3. run `python manage.py migrate`

## Create superuser for Admin app

1. python manage.py createsuperuser

## Register models with admin app

In order to modify the database and tables through the admin app you need to register the models in the `admin.py` within the respective app folder. For example, registering `blog` model:

1. In `blog_app` directory open `admin.py`.
2. Import models: `from .models import Blog`
3. Add: `admin.site.register(Blog)`

## Populating database with testing data

- `python manage.py populate_categories_and_tags` --> Adding initial Categories and Tags

## Function based handlers

See `blog_app/views.py`:

- Only when you have function based views do you use `api_views`:
  - `from rest_framework.decorators import api_view`

## Research How Cors Works

Building a user authentication app with React and Django Rest Framework -> https://www.youtube.com/watch?v=diB38AvVkHw

Custom Auth vs built in auth

- Watch above video for custom views for auth
- The following video imports the auth views (created by django): https://www.youtube.com/watch?v=bLGAKqn_stA&list=PLKnjLEpehhFlspe6zU1yyx5HDvPVDWMBe&index=48
