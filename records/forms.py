from django import forms

# test later
class CandForm(forms.Form):
    fName = forms.CharField(label= "First Name", max_length=100)
