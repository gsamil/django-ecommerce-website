## 1. Setup

```
>> git clone https://github.com/justdjango/django_project_boilerplate
>> cd ./django_project_boilerplate
```

#### Open folder in VsCode, create a virtual-env and activate it

- in cmd (Python must be installed):
```
>> py -m venv env
>> .\env\Scripts\activate
```

#### Install requirements

- in cmd
```
>> python -m pip install --upgrade pip
>> pip install -r requirements.txt
```

#### Rename project
```
>> python manage.py rename demo djecommerce
>> python manage.py migrate
```

#### Run server
```
>> python manage.py runserver
```

#### Authentication page

```
>> pip install django-allauth
```

- Add necessary lines from [documentation](https://django-allauth.readthedocs.io/en/latest/installation.html) to ``settings.py`` and ``urls.py``. Then do migration.
- Go to : http://127.0.0.1:8000/accounts/login/ login as superuser.

#### Create superuser

```
>> python manage.py createsuperuser
```

## 2. Project Configuration

### Create Models

- This is going to be everthing that defines the logic of storing an order, process of adding an item to an order.

## References:

[How to Build an E-commerce Website with Django and Python](https://youtu.be/YZvRrldjf1Y)