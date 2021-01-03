from django.shortcuts import render
from .models import *
from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.views.generic import *
from django.views.generic.edit import *
from django.db.models import Q
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
class SearchResultsView(ListView):
	model = new_sg
	template_name = 'main/result.html'
	def get_queryset(self):
		query = self.request.GET.get('q')
		object_list = new_sg.objects.filter(Q(artist__username__icontains=query))
		return object_list
		


class CreatePostView(CreateView):
	model = new_sg
	fields = ['song','add_mus','text', 'genre']
	def form_valid(self,form):
		form.instance.artist = self.request.user
		return super().form_valid(form)

class CreateOpisView(CreateView):
	model = opisan
	
	fields = ['img','text', 'city']
	success_url = 'accounts/mycab/'
	
	def form_valid(self,form):
		form.instance.artist = self.request.user
		form.instance.boo = True
		return super().form_valid(form)

class OpisEdit(LoginRequiredMixin, UpdateView):
	model = opisan
	
	success_url = '/accounts/mycab'
	fields = ['img','text', 'city']
	template_name = 'main/lk_edit_form.html'
	
	def form_valid(self, form):
		if form.instance.artist == self.request.user:
				return super().form_valid(form)
		else:
			return HttpResponseRedirect('/main/')

class PostDeleteView(DeleteView):
	model = new_sg
	success_url = 'main/'
	template_name = 'main/post_confirm_delete.html'

class PostEditView(UpdateView):
	model = new_sg
	
	fields = ['song','add_mus','text', 'genre']
	success_url = '/main'
	template_name = 'main/edit_form.html'

    
def main(request):
	
	track = new_sg.objects.all()
	#take = new_sg.objects.get(pk = new_sg_id)
	genre = rub.objects.all()
	user_on = User.objects.all()

	context = {'track' : track,'user_on':user_on,'genre' : genre,}
	return render(request,'main/main.html',context)

def Lk(request):
	us = request.user
	opis = opisan.objects.filter(artist = us.id)
	bbs = new_sg.objects.filter(artist = us.id)
	result = opisan.objects.filter(artist = us.id).exists()
	context = {'bbs' : bbs,'opis': opis, 'result' : result}
	return render(request,'main/lk.html',context)

def viewuser(request,user_id):
	
	opis = opisan.objects.filter(artist = user_id)
	bbs = new_sg.objects.filter(artist = user_id)
	context = {'bbs':bbs,'opis': opis}
	return render(request,'main/view_user.html',context)

def reg_user(request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
            # Create a new user object but avoid saving it yet
			new_user = user_form.save(commit=False)
            # Set the chosen password
			new_user.set_password(user_form.cleaned_data['password'])
            
            
			
			new_user.save()
			return render(request, 'main/register_done.html', {'new_user': new_user})
	else:
		user_form = UserRegistrationForm()
	return render(request, 'main/register.html', {'user_form': user_form})


def sort_by_g(request,rub_id):
	bbs = new_sg.objects.filter(genre = rub_id)
	current = rub.objects.get(pk = rub_id)
	genre = rub.objects.all()
	context = {'bbs' : bbs,'current' : current,'genre' : genre}
	return render(request,'main/view_rub.html',context)
 
	
# Create your views here.

