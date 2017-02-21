from django import forms

class ShareForm(forms.Form):
      text = forms.CharField(max_length=1220,widget= forms.Textarea({ "placeholder": "Write your experience..","required":"True","class":"form-control","rows":6,"cols":160}))
      doctor = forms.CharField(required=False,max_length=220,widget= forms.TextInput({ "placeholder": "Specify doctor if any..","class":"form-control","rows":6,"cols":160}))
      regno = forms.IntegerField(required=False,widget= forms.TextInput({ "default":0,"placeholder": "Specify register number of doctor..","class":"form-control","rows":6,"cols":160}))
      place = forms.CharField(required=False,max_length=220,widget= forms.TextInput({ "placeholder": "Specify the place..","class":"form-control","rows":6,"cols":160}))
      institution = forms.CharField(required=False,max_length=220,widget= forms.TextInput({ "placeholder": "Specify Institution if any...","class":"form-control","rows":6,"cols":160}))


