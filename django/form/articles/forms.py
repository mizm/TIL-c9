from django import forms
from .models import Article

class ArticleForm(forms.Form) :
    title = forms.CharField(label="제목", max_length=100)
    content = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 5,
        'cols' : 50,
        'placeholder':'내용을 입력하세요.',
        
    }))

class ArticleModelForm(forms.ModelForm) :
    title = forms.CharField(label="제목")
    class Meta :
        model = Article
        fields = ['title','content']