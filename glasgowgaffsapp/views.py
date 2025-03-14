from django.shortcuts import render
from django.http import HttpResponse
from glasgowgaffsapp.forms import UserForm,EventForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect
from glasgowgaffsapp.models import Event
from django.shortcuts import get_object_or_404   


def index(request):
    context_dict = {'boldmessage': ''}
    return render(request, 'glasgowgaffsapp/index.html', context=context_dict)

def create(request):
    if not request.user.is_authenticated:
        return redirect(reverse('glasgowgaffsapp:login'))
    
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect(reverse('glasgowgaffsapp:index'))
    else:
        form = EventForm()
    
    return render(request, 'glasgowgaffsapp/create.html', {'form': form})

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

def contact_us(request):
    context_dict = {'boldmessage': ''}
    return render(request, 'glasgowgaffsapp/contact.html', context=context_dict)

def events(request):
    all_events = Event.objects.all()
    return render(request, 'glasgowgaffsapp/events.html', {'events' : all_events})

def event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'glasgowgaffsapp/event.html', {'event': event})


@login_required
def myevents(request):
    created_events = Event.objects.filter(created_by=request.user)
    attending_events = Event.objects.filter(attendees=request.user)

    return render(request, 'glasgowgaffsapp/myevents.html', {
        'created_events': created_events,
        'attending_events': attending_events
    })

