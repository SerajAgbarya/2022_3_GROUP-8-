# CDFI PROJECT 
#####Last Updated: 14-Jan-2023

# Installation Guide

#### Pre install required packages

1. run `pip install django`


#### Steps:
#### if you download the system for first time:
1. `python manage.py createsuperuser`
2. `python manage.py migrate`
3. `python manage.py runserver`

#### In case you face issues with migrate (due installing system more than once or in case you want to have start all from start:
or if u dont work on clear DB. 
1. `python manage.py createsuperuser`
2. `python  manage.py migrate members zero --fake`
3. `python  manage.py migrate app zero --fake`
4. `python manage.py migrate`
5. `python manage.py runserver`

option3:
1. drop all tables from local db.
then run all steps above.


#### notes:

1. if failed with
   `from six import text_type ModuleNotFoundError: No module named 'six'`
   -> fix by : `python -m pip install six`
2.  if failed with -> `no widget-tweaks` ->fix by: `pip install django-widget-tweaks`
3. if you run by mistake higher version of migration , (or if you want to recreate all tables from scratch)
   you can reinstall the all migration by for the specific module (app or members):
    1. drop your tables manually from the database
    2. run `python3 manage.py migrate app zero --fake`
    3. run migration again `python3 manage.py migrate`

## Unit Tests:

1. run tests for app module `python3 manage.py test app.tests --settings=cdfi.settings`

### Test Coverage 
for app module test:
1. run `pip install coverage` (or use pip3 based on what u have)
2. run for example: `coverage run manage.py test app.tests --settings=cdfi.settings`
3. to get results: run `coverage report` or `coverage html` 



## For new developments

### Create New Model

1. in order to create new model , first create class for your model inside models.py
2. then run `python3 manage.py makemigration`
   ==> after this you should see new file generated under migration directory.

### General Development Notes

1. in case you created new directory/package u must have __init__.py The __init__.py should be an empty file (this tells
   Python that the directory is a package)


### Data base
1. shift shift `->` Action `->` plugins `->` database navigator `->` install `->` DB browser `->` plus button `->` SQLite `->` 
Database files `->` main `->` 3 dots `-> `choose db.sqlite3 from your project `->` test connection `->` apply `->` ok                      