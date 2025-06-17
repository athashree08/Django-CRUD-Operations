# Django-CRUD-Operations
Django - DJANGO is a high level web framework written in python.
Great for building robust, scalable web apps quickly
# Features :
ORM - Object relational mapping lets you interact with the Database using python instead of writing raw SQL queries
Admin Dashboard
Authentication System
URL routing
Template Engine

#Steps to Perform CRUD Operations:
prerquisites

1. Install Python
2. Install Django
3. Install Pychram

C - Create :
step 1: Create a new project
        Open terminal -> cmd 1 : pip install django
                         cmd 2 : django-admin startproject website
                         //website is the django project
                         cmd 3 : cd website
                         cmd 4 : python manage.py startapp web
                         // web is the django app -> django app is a standalone application that you can plug 
step 2: App created now link app to django project 
        go to settings.py in website(Django project)
        look for -> INSTALLED_APPS = [ ..... ,web] -> add django app name(web) at the end of list
        //This will install the application and allow Django project to view any code we put in Django app
#Create Operation Complete
DJANGO - MYSQL Connectivity : (prerequisites: install mysql)
Step 3: Enter command -> cmd 1 : pip install mysqlclient
Step 4: create database in mysql -> open mysql command line cliend 
                                    enter password
                                    cmd 1: create database mydjango;
step 5: go to settings.py 
        look for  [DATABASES = {
                                  'default': {
                                      'ENGINE': 'django.db.backends.mysql',
                                      'NAME': 'mydjango',
                                      'USER': 'enter username',
                                      'PASSWORD': 'enter password',
                                      'HOST': 'localhost',
                                      'PORT': 'port no.',
                                  }        
step 6: Now we have to create table 
        Go to model.py -> from django.db import models
                            class Student(models.Model):
                                name = models.CharField(max_length=100)
                                age = models.IntegerField()
                                class Meta:
                                    db_table = 'student'
step 7: in terminal enter command -> cmd 1 : python manage.py makemigrations
                                     cmd 2 : python manage.py migrate
                                     //use these commands everytime changes are made to apps.py
// Django - mysql connectivity completed

#FILE STRUCTURE :
website
  web
    migrations 
    templates -> contains html templates
      web
        register.html
        viewst.html
      _init__.py
      admin.py -> allows user to register DB models
      apps.py 
      models.py -> contains database models
      tests.py
      urls.py(add this file manually)
      views.py -> we can create different views that we can access on our website
    website
      _init__.py -> tells python to treat this directory like a python package
      asgi.py -> asynchronous server gateway interface
      settings.py -> contains different settings like installed apps, database configuration,                          static files , templates ,middleware , etc
      urls.py -> maps urls.py to views.py
      wsgi.py -> web server gateway interface is a special configuration file it allows django                    to communicate with the web server
    manage.py -> acts like command line tools - allows us to give commands to do things like DB                   migrations or run python server

#use "python manage.py runserver" to run server
      

        
        

