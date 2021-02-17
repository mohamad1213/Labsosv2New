from django.forms import ModelForm

from . import models

class StafForm(ModelForm):
    class Meta :
        model = models.Staf
        exclude=[]