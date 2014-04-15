from django import forms
from blog.models import Comment, Post

class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea)
    author = forms.CharField(max_length=60, required=False)
    
    
    class Meta:
        
        model = Comment
        exclude = ['post']

    def clean_author(self):

        return self.cleaned_data.get('author') or "Anonymous"
        
       


        
