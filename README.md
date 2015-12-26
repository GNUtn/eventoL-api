# eventoL-api
-------------

## Der
![Der](http://www.gliffy.com/go/publish/image/9317073/M.png)

## Notes:
docker run --name eventol-postgres -e POSTGRES_PASSWORD=secret -e POSTGRES_USER=eventol -e POSTGRES_DB=eventol -p 5432:5432 -d postgres
python manage.py makemigrations app
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
python manage.py test app
