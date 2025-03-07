from django.shortcuts import render
from django.http import HttpResponse
from glasgowgaffsapp.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect


def index(request):
    context_dict = {'boldmessage': ''}
    return render(request, 'glasgowgaffsapp/index.html', context=context_dict)

def create(request):
    if not request.user.is_authenticated:
        return redirect(reverse('glasgowgaffsapp:index')) 
    
    context_dict = {'boldmessage': ''}
    return render(request, 'glasgowgaffsapp/create.html', context=context_dict)

def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('glasgowgaffsapp:index')) 

    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True

            login(request,user)

            return redirect(reverse('glasgowgaffsapp:index'))
        
        else:
            print(user_form.errors)
    
    else:
        user_form = UserForm()
    
    return render(request,'glasgowgaffsapp/register.html',context = {'user_form': user_form, 'registered': registered})

def user_login(request):
    if request.user.is_authenticated:
        return redirect(reverse('glasgowgaffsapp:index')) 
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('glasgowgaffsapp:index'))
            else:
                return HttpResponse('Your GlasgowGaffs account is disabled.')
            
        else:
            return HttpResponse("Invalid login details supplied.")
    
    else:
        return render(request, 'glasgowgaffsapp/login.html')
    
@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('glasgowgaffsapp:index'))