
from django import forms


class fm(forms.Form):

    CHOICES = [
        ('1', 'Yes'),
        ('0', 'No'),
    ]

    CHOICES_1 = [
        ('0', 'Male'),
        ('1', 'Female'),
        ('2', 'Others'),
    ]

    Age = forms.CharField(widget=forms.NumberInput)
    Gender = forms.ChoiceField(widget=forms.RadioSelect,choices=CHOICES_1,)
    Genetic_Risk = forms.ChoiceField(widget=forms.RadioSelect,choices=CHOICES,)
    Smoking = forms.ChoiceField(widget=forms.RadioSelect,choices=CHOICES,)
    Chest_Pain = forms.ChoiceField(widget=forms.RadioSelect,choices=CHOICES,)
   
    Coughing_of_Blood = forms.ChoiceField(widget=forms.RadioSelect,choices=CHOICES,)
    Dry_Cough = forms.ChoiceField(widget=forms.RadioSelect,choices=CHOICES,)
    

