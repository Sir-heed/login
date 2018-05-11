from time import sleep

from django.shortcuts import (render, redirect, HttpResponse, 
HttpResponseRedirect, get_object_or_404)

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from django.contrib import messages

from .models import Post, Collection
from .forms import HomePageLoginForm, EditPostForm, SaveToCollectionForm

def country_cleaned():
	country_sel = Post()
	country = country_sel.COUNTRIES
	return country

def home(request):
	if request.method == "POST":
		form = HomePageLoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username=cd['username'],
			password=cd['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect("/dashboard/verified/")
				else:
					return HttpResponse("Disabled account.")
			else:
				return HttpResponse("Invalid Login")
	else:
		form = HomePageLoginForm()
	context = {"form": form}
	return render(request, "login.html", context)

@login_required	
def index(request):
	posts = Post.objects.all()
	checked_post = request.POST.getlist('checkbox')
	if 'checkbox' in request.POST:
		if 'submit' in request.POST:
			values = []
			for i in checked_post:
				values.append(int(i))
			collections = []
			for i in values:
				selected_post = Post.objects.get(pk=i)
				collections.append(selected_post)

		context = {"collections": collections}
		return render(request, "dashboard/ppost.html", context)
	else:
		form = SaveToCollectionForm(request.POST)
		if request.method == "POST":
			if form.is_valid():
				form.save()
				
		context = {"posts": posts, "countries": country_cleaned(), "form": form}
		return render(request, "dashboard/collections.html", context)
		
def verified(request):
	sleep(0.5)
	return redirect("/dashboard/index/")
	index(request)

def logout_view(request):
	logout(request)
	return home(request)


def post_detail_edit(request, post):
	post = get_object_or_404(Post, slug=post)

	if request.method == "POST":
		form = EditPostForm(request.POST, instance=post)
		if form.is_valid():
			# cd = form.cleaned_data
			# summary = cd["summary"]
			# summary.save()
			form.save()
			return HttpResponseRedirect("/dashboard/index")
	else:
		form = EditPostForm(instance=post)

	context = {
		"form": form,
		"post": post
		}
	return render(request, "dashboard/edit.html", context)