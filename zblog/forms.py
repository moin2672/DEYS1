from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')
choices_list=[]

for item in choices:
    choices_list.append(item)

class PostForm(forms.ModelForm):
    # author = forms.ChoiceField(widget=forms.HiddenInput())

    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category','body','snippet')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            # 'author': forms.TextInput(attrs={'class':'form-control', 'placeholder':'user name', 'value':'', 'id':'author_id', 'type':'hidden'}),
            'author': forms.Select(attrs={'class':'form-select'}),
            'category': forms.Select(choices=choices,attrs={'class':'form-select'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'snippet': forms.Textarea(attrs={'class':'form-control'}),
        }
        labels={
            'body':'Write your content here:'
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'snippet')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'snippet': forms.Textarea(attrs={'class':'form-control'}),
        }
        labels={
            'body':'Write your content here:'
        }
