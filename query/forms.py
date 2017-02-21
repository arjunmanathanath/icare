from django import forms
from . models import Query
class PostQuery(forms.Form):
    query_text = forms.CharField(max_length=150,widget= forms.Textarea({ "placeholder": "Enter Your Questions here...","required":"True","class":"form-control","rows":'7',"cols":'150',"id":"question","width": "830px", "height": "158px"}))

    #style = "width: 830px; height: 158px;"

class PostSolutions(forms.Form):
    soln_text = forms.CharField(max_length=9500,widget= forms.Textarea({ "placeholder": "Enter Your answer here...","required":"True","class":"form-control","rows":'7',"cols":'150',"id":"question","width": "830px", "height": "158px"}))

