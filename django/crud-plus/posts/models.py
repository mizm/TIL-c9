from django.db import models

# Create your models here.
class Post(models.Model) :
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    def __str__(self) :
        return self.title

class Student(models.Model) :
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    birthday = models.DateField()
    age = models.IntegerField()

# Post : Comment = 1 : N
class Comment(models.Model) :
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    
    def __str__(self):
        return self.content
    # on_delete 옵션
    # 1. CASCADE : 부모가 삭제되면, 자기 자신도 삭제
    # 2. PROTECT : 자식이 존재하면, 부모삭제 불가능.
    # 3. SET_NULL : 부모가 삭제되면 자식의 부모 정보를 NULL로 변경
'''
1. craete
post = Post(title='Hello', content='world!')
post.save()

2. Read
2.1. All
posts = Post.objects.all()

2.2. Get one
post = Post.objects.get(pk=1)

2.3. filter( WHERE )
posts = Post.objects.filter(title='Hello').all()
post = Post.objects.filter(title='Hello').first()

2.4. LIKE
posts = Post.objects.filter(title__contains='He').all()

2.5.order_by(정렬)
posts = Post.objects.order_by('title').all() #오름차순
posts = Post.objects.order_by('-title').all() #내림차순

2.6. limit & offset
[offset:offset+limit]
posts = Post.objects.all()[1:2]

3. Delete
post = Post.objects.get(pk=2)
post.delete()

4. update
post = Post.objects.get(pk=1)
post.title = 'hi'
post.save()

'''
