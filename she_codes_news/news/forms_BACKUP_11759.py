from django import forms
from django.forms import ModelForm
from .models import NewsStory
from django.utils import timezone,dateformat


class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ["title", "pub_date", "content", "image", "category"]
<<<<<<< HEAD
        widgets = {'pub_date': forms.DateInput(format=('%Y-%m-%d'),attrs={'class':'form-control', 'placeholder':'Select a date','type':'date', 'value': lambda: dateformat.format(timezone.now(), "Y-m-d"),},),
        }

=======
        # widgets = {'pub_date': forms.DateInput(format=('%Y-%m-%d'),attrs={'class':'form-control', 'placeholder':'Select a date','type':'date', 'value': lambda: dateformat.format(timezone.now(), "Y-m-d"),},),
        # }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pub_date'].initial = timezone.now().strftime("%Y-%m-%dT%H:%M")
>>>>>>> add-migrations
