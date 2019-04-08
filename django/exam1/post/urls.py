from django.urls import path
from post import views

app_name = 'post'

urlpatterns = [
    path('',views.index, name='index'),
    path('datail/<int:post_id>',views.detail, name='detail'),
    path('new/',views.new, name='new'),
    path('delete/<int:post_id>', views.delete, name='delete'),
]