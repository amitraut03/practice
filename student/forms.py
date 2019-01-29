from django import forms
from . import models

class Student_form(forms.ModelForm):
    class Meta:
        model=models.Student
        fields = ('name','rollno','branch')
