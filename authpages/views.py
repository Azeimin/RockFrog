from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.views.generic import View
from .forms import *
from django.contrib.auth import login

# Create your views here.
def index(request):
    template = loader.get_template('authpages/login.html')
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        context = {}
        return HttpResponse(template.render(context, request))
def logoutview(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")

class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect("/")
        else:
            template = loader.get_template('authpages/login.html')
            form = LoginForm()
            context = {'form' : form}
            return HttpResponse(template.render(context, request))
    def post(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect("/")
        else:
            bound_form = LoginForm(request.POST)

            if bound_form.is_valid():
                if(bound_form.DoAuth()):
                    login(request, bound_form.DoAuth())
                    return HttpResponseRedirect("/")
                else:
                    template = loader.get_template('authpages/login.html')
                    return HttpResponse(template.render({'form' : bound_form}, request))
            else:
                template = loader.get_template('authpages/login.html')
                return HttpResponse(template.render({'form' : bound_form}, request))


class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect("/")
        else:
            template = loader.get_template('authpages/register.html')
            form = RegistrationForm()
            context = {'form' : form}
            return HttpResponse(template.render(context, request))
    def post(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect("/")
        else:
            bound_form = RegistrationForm(request.POST)
            if bound_form.is_valid():
                user = bound_form.DoRegister()
                if(user):
                    login(request, user)
                    return HttpResponseRedirect("/")
                else:
                    template = loader.get_template('authpages/register.html')
                    return HttpResponse(template.render({'form' : bound_form}, request))
            else:
                template = loader.get_template('authpages/register.html')
                return HttpResponse(template.render({'form' : bound_form}, request))
