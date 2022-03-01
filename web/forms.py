from django import forms
from django.forms import TextInput
from .models import Student


class StudentsForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = [
            "name",
            "student_number",
        ]
        widgets = {
            'name': TextInput(attrs={'style': 'margin-bottom: 0px; margin-left: 20px'}),
            'student_number': TextInput(attrs={'style': 'margin-bottom: 0px'}),
        }