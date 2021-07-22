# Setup

## First time

If this is the first time setting up the project open the project folder in terminal and run these steps in terminal:

1. `python3 -m venv ~/.virtualenvs/djangodev`
1. `source ~/.virtualenvs/djangodev/bin/activate`
1. `python -m pip install Django`

## After first time

If you are opening the project back up run these steps in terminal:

1. `source ~/.virtualenvs/djangodev/bin/activate`

You should see `(djangodev)` in the beginning of your terminal line.

Now run: 

1. `python manage.py runserver`

You should see some lines appear, one of them being:

`Starting development server at http://127.0.0.1:8000/`