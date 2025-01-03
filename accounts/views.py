from django.shortcuts import render,HttpResponseRedirect,reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import SignUpForm
from django.db.models import Q

# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect(reverse('accounts:login'))
        form = AuthenticationForm()
        context = {'form': form}
        return render(request,'accounts/login.html',context)
    else:
        return HttpResponseRedirect(reverse('website:index'))

@login_required(redirect_field_name="") 
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('website:index'))

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('accounts:login'))
        form = SignUpForm()
        context = {'form':form}
        return render(request,'accounts/signup.html',context)
    else:
        return HttpResponseRedirect(reverse('website:index'))