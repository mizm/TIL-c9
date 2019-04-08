from django.urls import path
from posts import views
app_name = 'posts'
urlpatterns = [
    path('', views.index, name ='index'),
    path('new/', views.new, name = 'new'),
    path('detail/<int:post_id>/',views.detail, name='detail'),
    path('delete/<int:post_id>/', views.delete, name='delete'),
]
