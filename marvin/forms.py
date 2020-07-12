from django import forms
from .models import Post, Project

class ContactForm(forms.Form):
    email = forms.EmailField(label='Email address', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your@email.com'}), required=True)
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'class': 'form-control'}), required=True)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(
				attrs={
					'class': 'form-control'
					}
				),
            'text': forms.Textarea(
				attrs={
					'class': 'form-control'
					}
				),
			}

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'text', 'link', 'image')
        widgets = {
            'title': forms.TextInput(
				attrs={
					'class': 'form-control',
					}
				),
            'text': forms.Textarea(
				attrs={
					'class': 'form-control'
					}
				),
            'link': forms.TextInput(
				attrs={
					'class': 'form-control'
					}
				),
			'image': forms.FileInput(
				attrs={
					'class': 'form-control-file'
					}
				),
			}
