from django.forms import ModelForm,ClearableFileInput


from . import models

class ForumForm(ModelForm):
    class Meta :
        model = models.Forum
        exclude=['owner','waktu']

class PostingForm(ModelForm):
    class Meta :
        model = models.Posting
        exclude=['forum','owner','waktu'] 
        widgets = {
            'upload_img': ClearableFileInput(attrs={'multiple': True}),
        }

class KomenForm(ModelForm):
    class Meta:
        model = models.Komen
        exclude = ['posting','pengguna','waktu']

class BalasForm(ModelForm):
    class Meta:
        model = models.Balas
        exclude = ['komen','user','waktu']
