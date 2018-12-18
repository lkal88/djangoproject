from django import forms
from .models import Event
from tags.models import Tags
from subject.models import Subject
from django.forms import ModelForm, Form, ModelMultipleChoiceField
from django.forms.widgets import CheckboxSelectMultiple
import datetime
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
from tinymce import TinyMCE


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False



class EventCreateForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(mce_attrs={'width': 1000}))
    tags = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Tags.objects.all())
    subject = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Subject.objects.all())
    class Meta:
        model = Event
        fields = ['title', 'link', 'image', 'description', 'start', 'start_time', 'end_time', 'end', 'tags', 'subject']
        widgets = {
            'start': DatePickerInput(),
            'start_time': TimePickerInput(),
            'end': DatePickerInput(),
            'end_time': TimePickerInput(),
            #'description': forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30})),
        }
    #class Media:
    #    js = ('/media/tinymce/jscripts/tiny_mce/tiny_mce.js',
    #        '',)

#may have to change some of this stuff.
class EventUpdateForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(mce_attrs={'width': 1000}))
    tags = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Tags.objects.all())
    class Meta:
        model = Event
        fields = ['title', 'link', 'description', 'tags', 'subject']
        widgets = {
            'start': DatePickerInput(),
            'start_time': TimePickerInput(),
            'end': DatePickerInput(),
            'end_time': TimePickerInput(),
            #'description': forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30})),
        }


#'tags': forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,required=True),

#widgets = {
#    'startdate': forms.DateInput(attrs={'class':'datepicker'}),

#'start': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
#'end': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
#}



#    description = forms.CharField(
#        widget=TinyMCEWidget(
#            attrs={'required': False, 'cols': 30, 'rows': 10}
#        )
#    )
