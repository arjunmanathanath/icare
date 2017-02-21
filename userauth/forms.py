from django.forms import extras
from userauth.models import User
from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )


class LoginForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput({ "placeholder": "Password!","required":"True"}) )
    username = forms.CharField(max_length=20,widget= forms.TextInput({ "placeholder": "Username!","required":"True"}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        # user_qs = User.objects.filter(username=username)
        # if user_qs.count() == 1:
        #     user = user_qs.first()
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("oooopsss!!!!This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect passsword")
            if not user.is_active:
                raise forms.ValidationError("This user is not longer active.")
        return super(LoginForm, self).clean(*args, **kwargs)


class RegForm(forms.ModelForm):
    name = forms.CharField(max_length=50,widget=forms.TextInput({"placeholder":"Enter your Name","class":"form-control", "name":"name", "id":"name"}))
    password = forms.CharField(widget=forms.PasswordInput({"placeholder":"Enter your password","class":"form-control", "name":"password", "id":"password"}))
    cpassword = forms.CharField(widget=forms.PasswordInput({"placeholder":"Confirm your password","class":"form-control", "name":"confirm", "id":"confirm"}))
    birth_date = forms.DateField(widget=extras.SelectDateWidget(years=range(1950,2018)))
    email = forms.CharField(max_length=1200,widget=forms.TextInput({"placeholder":"Enter your Email","class":"form-control", "name":"email", "id":"email"}))
    country = forms.CharField(required=False,max_length=12,widget=forms.TextInput({"placeholder":"Enter location","class":"form-control", "name":"country", "id":"country"}))
    username = forms.CharField(max_length=50,widget=forms.TextInput({"placeholder":"Choose a username","class":"form-control", "name":"username", "id":"username"}))

    class Meta:
        model = User
        fields = ['name','username', 'email', 'mobile', 'birth_date', 'password', 'cpassword', 'country']

    def clean(self, *args, **kwargs):
         password = self.cleaned_data.get('password')
         cpassword = self.cleaned_data.get('cpassword')
         username = self.cleaned_data.get('username')
         if password != cpassword:
             raise forms.ValidationError("Passwords must match")
         username_qs = User.objects.filter(username=username)
         if username_qs.exists():
             raise forms.ValidationError("This email has already been registered")

         return super(RegForm,self).clean(*args, **kwargs)



class RForm(forms.Form):
    healthstatus =forms.CharField(max_length=120,widget=forms.TextInput({"placeholder":"for personalization enter disease name or 'healthy'","class":"form-control", "name":"healthstatus", "id":"healthstatus"}))

class Drform(forms.Form):
    reg_no = forms.IntegerField(widget=forms.TextInput({"placeholder":"Enter your register number","class":"form-control"}))
    qualification = forms.CharField(max_length=1200,widget=forms.TextInput({"placeholder":"qualification","class":"form-control", "name":"qualification", "id":"qualification"}))


