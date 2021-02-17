from django.forms import ModelForm
from bootstrap_datepicker_plus import DatePickerInput
from countable_field.widgets import CountableWidget
from crispy_forms.helper import FormHelper

from . import models

class PklForm(ModelForm):
    class Meta:
        model = models.Pkl
        exclude = [ 'approve','catatan','reject','owner','create_time','complete_time','approve2','reject2']
        widgets = {
            'tanggal_mulai': DatePickerInput(format='%d-%m-%Y').start_of('event days'),
            'tanggal_selesai': DatePickerInput(format='%d-%m-%Y').end_of('event days'),
        }
class RejectForm(ModelForm):
    class Meta:
        model = models.Pkl
        fields = ['reject','catatan']
        widgets = {
            'catatan': CountableWidget(attrs={'data-count': 'characters','data-max-count': 500, 'data-count-direction': 'down'}),                                            
        }

class UpdateForm(ModelForm):
    class Meta:
        model = models.Pkl
        exclude = [ 'approve','catatan','reject','owner','create_time','complete_time','approve2','reject2']
        widgets = {
            'tanggal_mulai': DatePickerInput(format='%d-%m-%Y').start_of('event days'),
            'tanggal_selesai': DatePickerInput(format='%d-%m-%Y').end_of('event days'),
        }
# class UpdateForm(ModelForm):
#     class Meta:
#         model = models.Pkl
#         fields = [ 'judul', 'nama_mitra','nama_dosen','tanggal_mulai','tanggal_selesai']
#         widgets = {
#             'tanggal_mulai': DatePickerInput(format='%d-%m-%Y').start_of('event days'),
#             'tanggal_selesai': DatePickerInput(format='%d-%m-%Y').end_of('event days'),
#         }
# class Reject2Form(ModelForm):
#     class Meta:
#         model = models.Pkl
#         fields = ['reject2','catatan']
#         widgets = {
#             'catatan': CountableWidget(attrs={'data-count': 'characters','data-max-count': 500, 'data-count-direction': 'down'}),                                            
#         }