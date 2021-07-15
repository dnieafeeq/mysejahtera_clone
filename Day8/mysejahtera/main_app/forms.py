from django import forms

from django.forms import fields
from .models import HealthInfo, Vaccine, QRLocation
from main_app import models
# from .models import profile


class HealthUpdateForm(forms.ModelForm):
    class Meta:
        model = HealthInfo
        fields = [
            'question1',
            'question2',
            'question3',
            'question4',
            'question5',
            'question6',
        ]
        labels = {
            "question1": "Question 1",
            "question2": "Question 2",
            "question3": "Question 3",
            "question4": "Question 4",
            "question5": "Question 5",
            "question6": "Question 6",
        }

    def __init__(self, *args, **kwargs):
        super(HealthUpdateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-sm'


class DateInput(forms.DateInput):
    input_type = 'date'


class VaccineForm(forms.ModelForm):
    class Meta:
        model = Vaccine
        fields = [
            'name',
            'age',
            'state',
            'date'
        ]
        widgets = {'date': DateInput()}

    def __init__(self, *args, **kwargs):
        super(VaccineForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-sm'


class QRCreateForm(forms.ModelForm):
    class Meta:
        model = QRLocation
        fields = [
            'name', 'address', 'city', 'state'
        ]

    def __init__(self, *args, **kwargs):
        super(QRCreateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-sm'
