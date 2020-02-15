# Python Django Async Chatting

Here using Python and Django, I have created a Chatting Application. For achieving Async behavior with Django, I have used Channels and Reddis database. The program has a simple database to store multiple people and then you can connect to them and start chatting. The program is also capable of doing group chatting.

## Getting Started

For starting the project, First, create a virtual environment for the python Lib's in the *requirement.txt* file.

``` cmd
python -m venv ./venv
```

*Activate* the virtual environment and download the required Lib's.

``` cmd
pip install -r requirement.txt
```

Before going any further, just create an SQLite file in the *current* folder and then *cd* into the folder and simply migrate and create the superuser in the database using Django.
And after doing this setup, run the server.

``` cmd
cd ./fastfood
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Basic Setup

Just go to <http://localhost:8000/admin> and Log in with your username and password that you have created in the createsuperuser part. Start creating some users and you will start seeing them in your list, select them and start chatting.

You will be required to install Reddis database on your computer for this to work.

## Build With

- Python - For working with Django
- Django - For creating the server
- Reddis - In-memory data structure store
- Channels - To handle WebSockets
- Django-crispy-forms

## Authors

**Aditya Mathur**, you can find me on [Twitter](https://twitter.com/mathuraditya7) or [LinkedIn](https://www.linkedin.com/in/aditya-mathur-7240/)

## License

This project is licensed under the MIT License
