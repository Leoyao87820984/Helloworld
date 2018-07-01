from django import forms
from .models import Post, Comment
from pagedown.widgets import PagedownWidget

class PostForm(forms.ModelForm):
	publish = forms.DateField(widget = forms.SelectDateWidget)
	text = forms.CharField(widget = PagedownWidget)
	class Meta:
		model = Post
		fields = ['title', 'summary','text','publish', 'type']
class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ('author', 'text',)