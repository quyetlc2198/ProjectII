from django import forms
from user.models import MyUser
from django.contrib.auth.forms import UserCreationForm



class RegisForm(UserCreationForm):
    email = forms.EmailField(required = True)
    
    class Meta:
        model = MyUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
    def save(self , commit = True):
        user = super(RegisForm, self).save(commit = False)
        user.first_name  = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()  
        return user

