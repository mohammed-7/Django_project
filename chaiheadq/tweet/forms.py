# we use forms in order to use the pre configd forms which django has.

from django import forms 
from .models import Tweet 

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text','photo']