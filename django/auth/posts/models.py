from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
#ResizeToFill 넘치느는 부분은 자름
#ResizeToFit 맞추고 남는 부분은 빈 공간으로 둠


# Create your models here.
class Post(models.Model) :
    title = models.CharField(max_length=100)
    content = models.TextField()
    # image = models.ImageField(blank=True)
    image = ProcessedImageField(
        upload_to='posts/images', #저장위치
        processors=[ResizeToFill(300,300)], #처리할 작업 목록
        format='JPEG',#저장 포맷
        options={'quality':95}, # 저장 포맷 관련 옵션
    )
    created_at = models.DateTimeField(auto_now_add=True) #create 될 때 딱 한번 현재 시각
    updated_at = models.DateTimeField(auto_now=True)# 변경이 될 때 마다 현재 시각
    
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
