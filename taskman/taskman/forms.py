from django import forms

class LoginForm(forms.Form):
	email = forms.EmailField(label="Email",max_length=100,widget=forms.EmailInput(
							attrs={'required':'true',
							'class':'form-control',
							'placeholder':'email'
							}))
	password = forms.CharField(label = "Password",widget=forms.PasswordInput(
							attrs={'required': 'true',
									'class':'form-control',
									'placeholder':'password'
									}))
class RegistrationForm(forms.Form):
	username = forms.CharField(label="Username",widget=forms.TextInput(
							attrs={'required':'true',
							'class':'form-control'}))
	email = forms.EmailField(label="Email",max_length=100,widget=forms.EmailInput(
							attrs={'required':'true',
							'class':'form-control'}))
	password = forms.CharField(label = "Password",widget=forms.PasswordInput(
							attrs={'required': 'true',
							'class':'form-control'}))
	confirm = forms.CharField(label = "Confirm",widget=forms.PasswordInput(
							attrs={'required': 'true',
							'class':'form-control'}),)