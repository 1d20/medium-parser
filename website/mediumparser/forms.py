from django.contrib.auth import authenticate, get_user_model
from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'


User = get_user_model()

class UsersRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "confirm_email", 
            "password",
        ]
    username = forms.CharField()
    email = forms.EmailField(label = "Email")
    confirm_email = forms.EmailField(label = "Confirm Email")
    password = forms.CharField(widget = forms.PasswordInput)


    def __init__(self, *args, **kwargs):
        super(UsersRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            "name":"username"})
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            "name":"email"})
        self.fields['confirm_email'].widget.attrs.update({
            'class': 'form-control',
            "name":"confirm_email"})
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            "name":"password"})


    def clean(self, *args, **keyargs):
        email = self.cleaned_data.get("email")
        confirm_email = self.cleaned_data.get("confirm_email")
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if email != confirm_email:
            raise forms.ValidationError("Email must match")
    
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("Email is already registered")

        username_qs = User.objects.filter(username=username)
        if username_qs.exists():
            raise forms.ValidationError("User with this username already registered")

        if len(password) < 8:	
            raise forms.ValidationError("Password must be greater than 8 characters")


        return super(UsersRegisterForm, self).clean(*args, **keyargs)