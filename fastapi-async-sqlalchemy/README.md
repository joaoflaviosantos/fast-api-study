# FastAPI, PostgreSQL, SQLAlchemy, AIOHTTP (Youtube Video)

[Video link](https://www.youtube.com/watch?v=1CZZAhwqyco)

## Dependecies
* Docker
* Docker-compse
* Python >= 3.6
* Pipenv

## How to run
Add project path at `PYTHONPATH` variable in `.env` file.

Start **postgres** database and **pgadmin**
```shell
docker-compose up -d
```

Start and activate virtual environment
```shell
virtualenv venv && ./venv/bin/activate
```

Install python dependencies
```shell
pip install -r requeriments.txt
```

Populate database
```shell
python populate.py
```

Start application
```shell
cd src/ && uvicorn main:app --port 8080
```

## Compare sync and async views
There are two versions of assets/day_summary endpoint, so you can compare both performance.
