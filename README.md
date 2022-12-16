# CDFI project

python3 manage.py createsuperuser 

python3 manage.py migrate

python3 manage.py runserver


notes:
1. if failed with 
     `from six import text_type ModuleNotFoundError: No module named 'six'`
   -> fix by : ` python -m pip install six`
