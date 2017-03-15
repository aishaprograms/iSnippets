# iSnippets
iSnippets, built with Django and Python, allows a user to create and view useful code snippets. Think of it as an app to keep track of idiomatic code samples in different languages.

## Technologies
- Python3
- pip
- virtualenv
- Django
- SQLite3
- Bootstrap / Bootswatch
- PostgreSQL

## Getting Started
Visit the Heroku app 
* **iSnippets** - [iSnippets](https://shrouded-river-56777.herokuapp.com/)

## Understand
This is an application that allows a user to create and save code snippets.
Each code snippet allows the user to record a title; the language the snippet is in; the snippet itself; and a brief description. 
This application uses Django's form helpers and generic views wherever possible.

## Tests
In order to run this locally, clone this repo then:
Create a virtual environment 
```
virtualenv venv
```

Activate the virtual environment  
```
source venv/bin/activate
```

Then while in the virtual environment... 

Install the application requirements with either of the following commands
```
pip3 install -r requirements.txt
pip3 manage.py runserver
```

Run the server at PORT 8000
```
python3 manage.py runserver
```

## Author
* **Aisha Ahmad** - [Aisha Ahmad](https://github.com/aishaprograms)

