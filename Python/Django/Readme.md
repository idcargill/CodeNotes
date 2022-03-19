# Django Setup

- (poetry init -n)
- poetry export -f requirements.txt -o requirements.txt --without-hashes

## Start Project

- create virtual environment

> poetry add Django

open project in current folder
> django-admin startproject <project_name> .

```python
# project/urls.pu
from django.urls import path, includes

urlpatterns = [
  path('', includes('snacks.urls')),
]
```

- Roger's "4" steps: Urls(app/project), Views, Templates, add app to project

### Project Level

> python manage.py startapp <name_app>

- add app to project settings INSTALLED_APPS
- add app to project urls
- create project template folder
- add template folder to project\
 'DIRS': [BASE_DIR /'templates'],

### APP Level

- build templates (project or app level)
- add app view
- add app urlpatterns

```python
# urls.py
from django.urls import path
from .views import HomePageView


urlpatterns = [
  path('', HomePageView.as_path(), name='home'),
  path('<int:pk>/', AppDetailView.as_view(), name='app_detail'),
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

```python
# app/admin.py
from django.contrib import admin
from .models import Movie

admin.site.register(Movie)

class Model(models.Model):
  owner         = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  name          = models.CharField(max_length=30)
  description   = models.TextField(default='')
  created_at    = models.DateTimeField(auto_now_add=True) # updated on creation
  updated_at    = models.DateTimeField(auto_now=True)  # updated current


```

Update

> python manage.py makemigrations <appName>

Update __str__ for model classes.

[View SQL with sqlitebrowser.org](https://sqlitebrowser.org/)

#### .env

> install django-environ

```python
# project settings.py
import environ

env = environ.Env(
  DEBUG=(bool, False)
)

SECRET_KEY = env.str('SECRET_KEY')

```

.env in project directory

Move to .env:

- SECRET_KEY = env.str('SECRET_KEY')
- DEBUG=TRUE
- ALLOWED_HOSTS=127.0.0.1,0.0.0.0,localhost

## PROJECT

### Settings.py

```python

INSTALLED_APPS = [
  '<newappname>,
]

```

### models.py

- create model
- add model to admin.py
- update database

> python manage.py makemigrations appName

> python manage.py migrate  

```python
# project/models.py
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Movie(models.Model):
  name = models.CharField(max_length=64)
  description = models.TextField(default='')
  owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  
  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('movie_detail', args=[str(self.id)])


# project/admin.py
from django.contrib import admin
from .models import Movie

admin.site.register(Movie)
```

#### Templates

- Add Static folder
- add static folder location to settings.py

- movie-create.html
- movie-delete.html
- movie-detail.html
- movie-update.html

to HTML files add:
> {% load static %}

templates/

- base.html\
add CDN  and STATIC to base.html

```python
# project/settings.py

TEMPLATES add Template BASE_DIR / templates
DIRS = [BASE_DIR / 'templates']
```

```html
{% load static %}
<!-- base.html -->
<link rel='stylesheet' href="{% static 'base.css' %}">

<header>
    <h1><a href="{% url 'movie_list' %}">Full Movies</a></h1>
  </header>

  {% block content %}
    <p>Default html stuff</p>
  {% endblock content %}


<!-- movies-create.html -->
{% extends base.html %} 

  {% block content %}
    <p>Default html stuff</p>
  {% endblock content %}



<!-- movie_list.html   LIST VIEW -->
{% extends base.html %} 

  {% block content %}
    <ul>
      {% for movie in object_list %}
        <li>
          <a href="{% url 'movie_detail' movie.pk %}">{{ movie.name }}</a>
        </li>
      {% endfor %}
    </ul>


  {% endblock content %}


```

#### Views

```python
# app/views.py

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Movie
from django.urls import reverse_lazy

class MovieListView(ListView):
  template_name = 'movie_list.html'
  model = Movie

class MovieDetailView(DetailView):
  template_name = 'movie_detail.html'
  model = Movie

# needs extra fields (match model)
class MovieCreateView(CreateView):
  template_name = 'movie_create.html'
  model = Movie
  fields= ['name', 'description', 'owner']

# needs fields
class MovieUpdateView(UpdateView):
  template_name = 'movie_update.html'
  model = Movie
  fields= ['name', 'description', 'owner']

# update URL after form submission in view
class MovieDeleteView(DeleteView):
  template_name = 'movie_delete.html'
  model = Movie
  success_url = reverse_lazy('list_view')


#### API
class ApiClass(generics.ListAPIView):
  queryset = Thing.objects.all()
  serializer_class = AppSerializer


class AppDetail(generics.RetrieveAPIView):
  queryset = Thing.objects.all()
  serializer_class = AppSerializer

### delete previous view. 
class AppDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Thing.objects.all()
  serializer_class = AppSerializer

```

### urls.py

```python
# project/urls.py

urlpatterns = [
  path('movies/', include('movies.urls'))
]


# app/urls.py

from django.urls import path
from django.urls.resolvers import URLPattern
from .views import DetailView, ListView ...

urlpatterns = [
  path('', MovieListView.as_view(), name='list_view'),
  path('new', MoviesCreateView.as_view(), name='create_view'),
]
```

#### Django FORM

```html
<!-- create path: 'new'-->
{% extends base.html %} 

  {% block content %}
    <h2>FORM</h2>

    <form action="" method="POST">
      {% csrf_token %}
      {{ form.as_p }}
    <input type='submit' value='SAVE'>
    </form> 

  {% endblock content %}


<!-- update  path: '<int:pk>/edit'-->
{% extends base.html %} 

  {% block content %}
    <h2>FORM</h2>

    <form action="" method="POST">
      {% csrf_token %}
      {{ form.as_p }}
    <input type='submit' value='SAVE'>
    </form> 

  {% endblock content %}


<!-- delete path: '<int:pk>/delete'-->
{% extends base.html %} 


  {% block content %}
    <h2>FORM</h2>

    <form action="" method="POST">
      {% csrf_token %}
      {{ form.as_p }}
      <p>Do you want to delete {{ movie.name }}</p>
    <input type='submit' value='OK'>
    </form> 

  {% endblock content %}



<!-- movie_detail.html -->

```

#### CSS

#### REST API

> poetry add djangorestframework

add to INSTALLED_APPS

```python
# settings.py

REST_FRAMEWORK = { "DEFAULT_PERMISSION_CLASSES' : [
  'rest_framework.permisssions.AllowAny',
  ]
}
```

- Serializer

```python
from rest_framework import serializers
from .models import myModel

class ThingSerializer(serializers.ModelSerializer):
  class Meta:
    fields  = ('owner', 'id', 'name', ...)
    model   = myModel

```
