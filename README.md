# CDFI PROJECT 
#####Last Updated: 14-Jan-2023

# Installation Guide

#### Pre install required packages

1. run ``
2. run ``
3. run ``

#### Steps:

1. `python3 manage.py createsuperuser`
2. `python3 manage.py migrate`
3. `python3 manage.py runserver`

#### notes:

1. if failed with
   `from six import text_type ModuleNotFoundError: No module named 'six'`
   -> fix by : `python -m pip install six`
2. if you run by mistake higher version of migration , (or if you want to recreate all tables from scratch)
   you can reinstall the all migration by for the specific module (app or members):
    1. drop your tables manually from the database
    2. run `python3 manage.py migrate app zero --fake`
    3. run migration again `python3 manage.py migrate`

## Unit Tests:

1. run tests for app module `python3 manage.py test app.tests --settings=cdfi.settings`

## For new developments

### Create New Model

1. in order to create new model , first create class for your model inside models.py
2. then run `python3 manage.py makemigration`
   ==> after this you should see new file generated under migration directory.

### General Development Notes

1. in case you created new directory/package u must have __init__.py The __init__.py should be an empty file (this tells
   Python that the directory is a package)