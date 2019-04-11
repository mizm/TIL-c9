from django.urls import path
from . import views
from accounts import views as accounts_views

app_name = 'accounts'

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('<str:username>/',accounts_views.people, name='people'),
]