from django import forms

class StudentForm(forms.Form):
    Name=forms.CharField()
    marks=forms.IntegerField()


    