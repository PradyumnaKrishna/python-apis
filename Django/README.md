# Django API

This Web Application Contains Source Code of Django API.

## Deployed on Azure

Deployment in progress.

## Deployed on Heroku

The api is working fine, send requests to <http://mydjango-api.herokuapp.com/> .

## Run Server

To run, type:

```sh
python manage.py runserver
```

To test the application, type:

```sh
python manage.py test
```
*Only 1 test available yet

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