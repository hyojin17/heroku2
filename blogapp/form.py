from django import forms
from .models import Blog

class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog#블로그 모델을 기반으로
        fields = ['title', 'body']#제목과 내용을 입력받을 것이다.
