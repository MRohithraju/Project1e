from django import  forms

class Regform(forms.Form):
    fristname=forms.CharField(max_length=15)
    lastname=forms.CharField(max_length=15)
    username=forms.CharField(max_length=14)
    password=forms.CharField(max_length=12,widget=forms.PasswordInput())
    cpassword=forms.CharField(max_length=10,widget=forms.PasswordInput())
    emailid=forms.EmailField()
    mobileno=forms.IntegerField()
class LoginForm(forms.Form):
    username=forms.CharField(max_length=15)
    password=forms.CharField(max_length=15,widget=forms.PasswordInput())
