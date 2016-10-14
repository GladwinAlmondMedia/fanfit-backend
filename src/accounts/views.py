from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)
from django.shortcuts import render, redirect

# Create your views here.

from .forms import UserLoginForm, UserRegisterForm


def login_view(request):

	next = request.GET.get('next')

	title = "Login"

	form = UserLoginForm(request.POST or None)

	form_button = "Login"

	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		login(request, user)
		if next:
			return redirect(next)
		return redirect('/admin')

	context = {
		"form": form,
		"title": title,
		"form_button": form_button,
	}
	return render(request, "accounts_form.html", context)


def register_view(request):

	next = request.GET.get('next')

	title = "Register"

	form = UserRegisterForm(request.POST or None)

	if form.is_valid():
		new_user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		new_user.set_password(password)
		new_user.save()

		user = authenticate(username=new_user.username, password=password)
		login(request, user)
		if next:
			return redirect(next)
		return redirect('/admin')

	form_button = "Register"

	context = {
		"form": form,
		"title": title,
		"form_button": form_button,
	
	}
	return render(request, "accounts_form.html", context)


def logout_view(request):
	logout(request)
	return redirect('/admin')
	context = {
		"title": "Logout",
	}
	return render(request, "accounts_form.html", context)




