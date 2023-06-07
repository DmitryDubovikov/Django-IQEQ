# Django-IQEQ

docker build -t iqeq .
docker run -it -v C:\projects\Django-IQEQ\:/app iqeq bash

poetry add django=3.2
django-admin startproject iqeq_project .

docker build -t iqeq .

docker run --rm -d -p 8000:8000 --name iqeq iqeq

docker run --rm -d -p 5432:5432 -v my-postgres-data:/var/lib/postgresql/data --name my-postgres my-postgres



docker build -t iqeq 
docker run --name iqeq -p 8000:8000 -v C:\projects\Django-IQEQ:/app iqeq

docker exec -it iqeq bash
python manage.py migrate