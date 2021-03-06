from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(label="Username", max_length=50, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
	password = forms.CharField(label="Password", max_length=50, widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class BlogPostForm(forms.Form):
	title = forms.CharField(label="Title", max_length=200)
	body = forms.CharField(label="Body", max_length=5000)

class SignupForm(forms.Form):
	username = forms.CharField(label="Username", max_length=50)
	first_name = forms.CharField(label="First Name", max_length=50)
	last_name = forms.CharField(label="Last Name", max_length=50)
	password = forms.CharField(label="Password", max_length=50, widget = forms.PasswordInput())
