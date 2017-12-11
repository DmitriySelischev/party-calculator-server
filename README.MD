## run app
```bash
pipenv install
pipenv shell
pipenv run src/manage.py runserver
```
## Docker
```bash
. .env
docker build -t $DOCKER_IMAGE_NAME .
```
