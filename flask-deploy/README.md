# FLASK + NGINX + GUNICORN + POSTGRESQL
## To run project locally:
```shell
docker-compose up -d --build
```
Flask app will be available at the localhost:
 - `http://localhost:5000/`

## To run project in production:
```shell
docker-compose -f docker-compose.prod.yml up -d --build
```
## If you run project first time you need to run next commands:
- `docker-compose exec web python manage.py create_db` - to create tables in database
- `docker-compose exec web python manage.py add_default_content_to_tables` - add inital data

Flask app will be available at the localhost:
 - `http://localhost:1337/`