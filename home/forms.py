from .models import Questionnaire
from django import forms

AGES = (
    0, "Select",
    1, "Below 18",
    2, "Above 18 and below 30",
    3, "Above 30 and Below 50",
    4, "Above 50"
)

GENDER = (
    0, "Select",
    1, "Male",
    2, "Female",
    3, "Rather not Say"
)


class QuestionnaireAdmin(forms.ModelForm):
    class Meta:
        model = Questionnaire
        fields = ('name', 'age', 'location')


class QuestionnaireForm(forms.Form):
    name = forms.CharField(max_length=200)
    gender = forms.IntegerField(choices=GENDER, default=0)
    age = forms.IntegerField(choices=AGES, default=0)
    location = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
