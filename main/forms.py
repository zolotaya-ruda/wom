from django.shortcuts import render
from .models import *
from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import *
from django.http import HttpResponseRedirect
from django.views.generic import *
from django.views.generic.edit import *
from django.db.models import Q
from django import forms
from django.contrib.auth.models import User
from .models import *
from django.forms.widgets import *
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    about = forms.CharField(label = 'О себе:', max_length=100)
    city = forms.ModelChoiceField(queryset = city.objects.all(), label = 'Город', widget = forms.Select(attrs = {'size':2}))
    class Meta:
        model = User
        fields = ('username','email')

class NewSong(forms.ModelForm):
	genre = forms.ModelChoiceField(queryset = rub.objects.all(), label = 'жанр',widget = forms.Select(attrs = {'size':2}))
	
	class Meta:
		model = new_sg
		fields = ('song','artist','add_mus','genre')

class lk(forms.ModelForm):
	city = forms.ModelChoiceField(queryset = city.objects.all(), label = 'Город',widget = forms.Select(attrs = {'size':2}))
	
	class Meta:
		model = opisan
		fields = ('img','text','city','artist',)
		
			
	
		
		


	