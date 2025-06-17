
````markdown
# Django-CRUD-Operations

Django - DJANGO is a high level web framework written in Python.  
Great for building robust, scalable web apps quickly.

---

## Features :

- ORM - Object Relational Mapping lets you interact with the database using Python instead of writing raw SQL queries  
- Admin Dashboard  
- Authentication System  
- URL Routing  
- Template Engine  

---

## Steps to Perform CRUD Operations:

**Prerequisites:**

1. Install Python  
2. Install Django  
3. Install PyCharm  

---

### C - Create :

**Step 1: Create a new project**  
```bash
pip install django
django-admin startproject website  # 'website' is the Django project
cd website
python manage.py startapp web      # 'web' is the Django app
````

> A Django app is a standalone application that you can plug into the main project.

**Step 2: Link app to Django project**
Go to `settings.py` in the Django project (`website`) and add this line:

```python
INSTALLED_APPS = [
    ...
    'web',  # add your app here
]
```

This will install the application and allow the Django project to detect any code we put in the Django app.

✅ **Create Operation Complete**

---

### DJANGO - MYSQL Connectivity :

*(Prerequisite: install MySQL)*

**Step 3:**

```bash
pip install mysqlclient
```

**Step 4:**
Open MySQL command-line client → Enter password →

```sql
create database mydjango;
```

**Step 5:**
Go to `settings.py` and configure your database:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydjango',
        'USER': 'your-username',
        'PASSWORD': 'your-password',
        'HOST': 'localhost',
        'PORT': 'your-port',
    }
}
```

**Step 6:**
Define your model in `models.py`:

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        db_table = 'student'
```

**Step 7:** Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

> Use these commands every time changes are made to `models.py`.

✅ **Django - MySQL Connectivity Completed**

---

## FILE STRUCTURE :

```
website/
│
├── web/
│   ├── migrations/
│   ├── templates/
│   │   └── web/
│   │       ├── register.html
│   │       └── viewst.html
│   ├── __init__.py
│   ├── admin.py          # allows user to register DB models
│   ├── apps.py           
│   ├── models.py         # contains database models
│   ├── tests.py
│   ├── urls.py           # (add manually)
│   └── views.py          # defines different views accessible on the website
│
├── website/
│   ├── __init__.py       # treat this as a Python package
│   ├── asgi.py           # asynchronous server gateway interface
│   ├── settings.py       # contains app settings, DB config, static files, etc.
│   ├── urls.py           # maps urls to views
│   └── wsgi.py           # web server gateway interface (communicates with web server)
│
└── manage.py             # command-line tool for DB migrations, running server, etc.
```

---

## Run Your Server

```bash
python manage.py runserver
```

✨ Now your Django CRUD app is up and running!

```
