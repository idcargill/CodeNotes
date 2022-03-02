# Django Setup

(poetry init -n)

## Start Project

- create virtual environment
- install Django
- django-admin startproject <project_name> .  # open project in current folder

- Roger's "4" steps: Urls(app/project), Views, Templates, add app to project

### Project Level

- python manage.py startapp <name_app>
- add app to project settings INSTALLED_APPS
- add app to project urls
- create project template folder
- add template folder to project
  > 'DIRS': [BASE_DIR /'templates'],

### APP Level

- build templates (project or app level)
- add app view
- add app urlpatterns

```python
from django.urls import path
from .views import HomePageView

urlpatterns = [
  path('', HomePageView.as_path(), name='home')
]
```

- add link to navigation
- add unit tests

### Server

- python manage.py runserver <port_optional>

### Superuser

> python manage.py createsuperuser

### Migrations

```python
python manage.py migrate
```

### Django Models

Register with admin.py in project.

Update

> python manage.py makemigrations <appName>

Update __str__ for model classes.

[View SQL with sqlitebrowser.org](https://sqlitebrowser.org/)
