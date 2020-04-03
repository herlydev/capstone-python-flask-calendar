Capstone Python Flask Calendar
as a back-end for a React app 
Marketing Lead Generation Landing page.
____________________________________________________________________________________________________

# Python Flask LEAD Api
> Python Flask backend app for keeping track of Lead.  It uses a flask sqlite database along with flask-marshmallow for object serialization/deserialization.  You can Post, Get, and Delete todos through flask routes.
- Dependencies
  - Python
    - [python](https://www.python.org/)
  - Flask
    - [flask-pypi](https://pypi.org/project/Flask/)
    - [flask-docs](https://flask.palletsprojects.com/en/1.1.x/)
  - Flask-SQLAlchemy
    - [flask-sqlalchemy-pypi](https://pypi.org/project/Flask-SQLAlchemy/)
    - [flask-sqlalchemy-docs](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
  - Flask-Marshmallow
    - [flask-marshmallow-pypi](https://pypi.org/project/flask-marshmallow/)
    - [flask-marshmallow-docs](https://flask-marshmallow.readthedocs.io/)

- Install all dependencies
```
$ pipenv install Flask Flask-SQLAlchemy flask-marshmallow
```
- Create your sqlite database
```
$ pipenv shell
$ python
>>> from app import db
>>> db.create_all()
```
- Flask Routes
  - POST One Todo
    - http://localhost:5000/lead
    ```
    {
        "fname": "Michael",
        "lname": "Jordan",
        "phone": "8012345678",
        "email": "air.mjordan@gmail.com"
    }
    ```
  - GET All Todos
    - http://localhost:5000/leads
  
    ```
  - DELETE One Todo
    - http://localhost:5000/lead/id