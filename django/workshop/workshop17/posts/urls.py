from django.urls import path
from . import views
from .models import Student
urlpatterns = [
    path('',views.index),
    path('new/',views.new),
    path('create/',views.create),
    path('<int:st_id>/',views.detail),
    path('<int:st_id>/delete/',views.delete),
    path('<int:st_id>/edit/',views.edit),
    path('<int:st_id>/update/',views.update),
    path('search/',views.search),
    path('<int:st_id>/write/',views.write),
    path('<int:rk>/write/send/',views.send),
]