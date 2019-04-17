from django.db import models

# Create your models here.
class Post(models.Model) :
    title = models.TextField()

# 정리
# class Post -> Django - Model / DB - Table
# post = Post() -> Django - Instance or Object / DB - Record or Row
# title -> Django - Field  / DB - Column
# 
# 마이그레이션 in terminal
# ./manage.py makemigrations
# ./manage.py migrate

# CRUD
# 1. Create
# 1) post = Post(title='hello-1')
#    post.save()
# 2) post2 = Post.objects.create(title='hello-2')
# 3) post3 = Post()
#    post3.title = 'hello-3' 
#    post3.save()

# 2. Read
# 2-1. All
# Post.objects.All()

# 2-2. Get
# 방법 1
# post.objects.get(id=1) pk = 1 , title='hello-1'
# 방법 2 (views.py 한정)
# from django-shortcuts import get_objects_or_404
# post = get_objects_or_404(Post,id=1) pk = 1 , title='hello-1'
# 방법 3
# post = Post.objects.filter(id=1)[0]  pk = 1 , title='hello-1'
# post = Post.objects.filter(id=1).first()

# 2-3. Where(filter)
# posts = Post.objects.filter(title='hello-1') 복수형
# post = Post.objects.filter(title='hello-1').first / [0]

# __contains : like(in sql)
# posts = Post.objects.filter(title__contains='lo') 

# Orderby -> orderby 실행시 정렬이 되니 검색 후 정렬
# posts = Post.objects.order_by('title')  제목 오름차순
# posts = Post.objects.order_by('-title') 제목 내림차순

# Offset & limit
# Post.objects.all()[0] > offset 0 limit 1
# Post.objects.all()[1] > offset 1 limit 1
# Post.objects.all()[1:3] > offset 1 limit 2
# Post.objects.all()[offset:offset+limit]

# 3. Update
# post = Post.objects.get(pk=1)
# post.title = 'hello-5'
# post.save() -> 실제 데이터베이스에 저장

# 4. Delete
# post = Post.objects.get(pk=1)
# post.delete()
