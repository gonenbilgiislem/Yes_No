from django import forms
from .models import Support

class SupportForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your name',}))
    problem = forms.CharField( widget=forms.Textarea(attrs={'rows':5, 'placeholder': 'Describe your problem here...'}))
    class Meta:
        model = Support
        fields = "__all__"