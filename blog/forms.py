from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'venue_image')
    
        labels={
            'title': 'Cím',
            'text': 'Könyv leírása',
            'venue_image': 'Kép a könyvről',
        }