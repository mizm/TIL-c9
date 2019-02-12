from django.urls import path
from . import views
app_name = 'article'

urlpatterns = [
    path('',views.index, name ='index'),
    path('menu/new/<str:kind>/',views.new, name ='new'),
    path('menu/',views.menu, name ='menu'),
    path('menu/<int:food_id>/',views.detail, name ='detail'),
]