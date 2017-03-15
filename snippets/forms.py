from django import forms

class SnippetForm(forms.Form):

    title = forms.CharField(label='Title', max_length=256)
    
    language = forms.CharField(label='Language', max_length=256)

    snippet = forms.CharField(widget=forms.Textarea, label='Snippet')

    description = forms.CharField(widget=forms.Textarea, label='Description')
