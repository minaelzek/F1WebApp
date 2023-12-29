# Project Title

A simple overview of use/purpose.

### Django Setup
```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

### Swagger docs
```
py manage.py spectacular --color --file schema.yml
```
Then go to http://localhost:8000/f1/api/schema/swagger-ui/ or  http://localhost:8000/f1/api/schema/redoc/

### Executing program

* How to run the Django server
```
python manage.py runserver
```

* How to run react project
```
npm start
```
