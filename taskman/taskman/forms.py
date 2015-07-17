from django import forms

class LoginForm(forms.Form):
	email = forms.EmailField(label="Email",max_length=100,widget=forms.TextInput(attrs={'required':'true'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'required': 'true'}),label = "Password")

class RegistrationForm(forms.Form):
	username = forms.CharField(label="Username",widget=forms.TextInput(attrs={'required':'true'}))
	email = forms.EmailField(label="Email",max_length=100,widget=forms.TextInput(attrs={'required':'true'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'required': 'true'}),label = "Password")
	confirm = forms.CharField(widget=forms.PasswordInput(attrs={'required': 'true'}),label = "Confirm")