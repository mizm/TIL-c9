from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # path('naver/<str:q>/',views.naver),
    path('',views.index, name='list'), #GET
    path('new/',views.new, name='new'), # get(new), Post(create)
    path('<int:post_id>/',views.detail, name='detail'), # GET
    path('<int:post_id>/delete/',views.delete, name='delete'), # GET(confirm), Post(delete)
    path('<int:post_id>/edit/',views.edit, name='edit'), #get(edit), post(update)
    # path('<int:post_id>/update/',views.update, name='update'), #
    path('<int:post_id>/comments/create/',views.comments_create, name='comments_create'),
    path('<int:post_id>/comments/delete/<int:comment_id>',views.comments_delete, name='comments_delete'),
]