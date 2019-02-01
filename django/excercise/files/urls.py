from django.urls import path
from . import views

app_name = 'files'

urlpatterns = [
    path('',views.index, name='index'),
    path('new_movie/',views.new_movie, name='new_movie'),
    path('create_movie/',views.create_movie, name='create_movie'),
]