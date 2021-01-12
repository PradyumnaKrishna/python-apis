# Flask API

This Web Application Contains 5 Python files and 1 Database File.

- `app.py`: This file registers blueprints of all flask api created (e.g. items) and initialize the flask applicaiton.
- `items.py`: API for question 1, It contains a flask blueprint of API
- `booking.py`: API for question 2, It contains a flask blueprint of API
- `plot.py`: API for question 3, It contains a flask blueprint of API
- `database.py`: Initialize Database using SQLAlchemy and Marshmallow
- `app-test.py`: Code to test this web application using provided example Request/Response in question.

## Deployed on Azure

send request to <http://flask-apis.azurewebsites.net> because I have deployed this eb application on Azure.

## Deployed on Heroku

Database wasn't working on Azure, that's why I came to Heroku. The api is working fine, send requests
to <http://myflask-api.herokuapp.com/> .

## Run Server

To run, type:

```sh
python app.py
```

To test the application, type:

```sh
python app-test.py
```

## `curl` Requests

### For Question 1

- POST /items

```sh
curl -X POST http://127.0.0.1:8000/items \
    -H 'Content-Type: application/json' \
    -d '[1, 4, -1, "hello", "world", 0, 10, 7]'
```

### For Question 2

- POST /booking

```sh
curl -X POST http://127.0.0.1:8000/booking \
    -H 'Content-Type: application/json' \
    -d '{"slot":2, "name":"Rick"}'
```

- GET /booking

```sh
curl http://127.0.0.1:8000/booking
```

- POST /cancel

```sh
curl -X POST http://127.0.0.1:8000/cancel \
    -H "Content-Type: application/json" \
    -d '{"slot":2, "name":"Rick"}'
```

### For Question 3

- POST /plot

```sh
curl -X POST http://127.0.0.1:8000/plot \
    -H "Content-Type: application/json" \
    -d '{"x":5, "y":5}'
```