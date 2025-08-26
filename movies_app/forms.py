from django import forms
from .models import Director, Movie
import datetime

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'


class MovieForm(forms.ModelForm):
    duration = forms.DurationField(
        required=True,
        help_text="Formato: HH:MM:SS",
        widget=forms.TextInput(attrs={'placeholder': 'HH:MM:SS'})
    )

    class Meta:
        model = Movie
        fields = '__all__'
        widgets = {
            'release_year': forms.DateInput(attrs={'type': 'date'}),
        }
