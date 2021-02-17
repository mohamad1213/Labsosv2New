from django.forms import ModelForm
from . import models
from forum.models import Forum
from forum.forms import ForumForm

class MitraForm(ModelForm):
    class Meta :
        model = models.Mitra
        exclude=['owner']