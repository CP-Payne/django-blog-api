For basic settup see notes on quick-todo

## Django Rest Framework (DRF)
Used to build RESTful APIs with Django.

DRF is composed of the following components:

1. Serializers are used to convert Django QuerySets and model instances to (serialization) and from (deserialization) JSON (and a number of other data rendering formats like XML and YAML).
2. Views (along with ViewSets), which are similar to traditional Django views, handle RESTful HTTP requests and responses. The view itself uses serializers to validate incoming payloads and contains the necessary logic to return the response. Viewsets are coupled with routers, which map the views back to the exposed URLs.

Installing django rest framework and django rest JWT:
```python
pip3 install djangorestframework markdown django-filter djangorestframework_simplejwt
```


## Create App

1. `python manage.py startapp <appName>`
2. register app in `settings.py` by adding it to `INSTALLED` list


## Using Postgres
1. Run `pip install psycopg2`
2. Update database variable in `settings.py`