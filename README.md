### Followed this tutorial
https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c

### Virtual environments

```
$ sudo apt-get install python-virtualenv
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install --upgrade pip
$ pip install django
$ pip install djangorestframework
```

### Create new project
```
django-admin startproject nexfac_core
cd nexfac_core
python manage.py runserver

python manage.py startapp nexfac_core_api
```

### DB migrate and superuser creation
```
python manage.py migrate
python manage.py createsuperuser

Email address: admin@nexfac.com
Password: coffee@321
```


### Tasks left -
[X] Add support for independent tasks
[X] Return tasks for users, currently only user details are returned

### Git
rm -rf .git
git init
git add .
git commit -m "First commit"
git remote add origin https://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@github.com/sarthak0415/django-nexfac-api-v1.git
