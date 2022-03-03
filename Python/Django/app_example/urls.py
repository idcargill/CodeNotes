from django.urls import path
from .views import MovieDetailsView, MovieListView

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('<int:pk>/', MovieDetailsView.as_view(), name='movie_detail'),
]
