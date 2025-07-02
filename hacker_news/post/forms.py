from django import forms

class PostForm(forms.Form):
    title = forms.CharField(max_length=128, label="제목")
    body = forms.CharField(max_length=1024, label="본문")
    author_name = forms.CharField(max_length=32, label="작성자")