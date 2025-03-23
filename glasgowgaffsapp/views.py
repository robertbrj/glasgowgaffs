from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from glasgowgaffsapp.forms import UserForm, EventForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect
from glasgowgaffsapp.models import Event
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail


def index(request):
    """
        view for the homepage.
        renders the index.html template
    """
    context_dict = {'boldmessage': ''}
    return render(request, 'glasgowgaffsapp/index.html', context=context_dict)


@login_required()
def create(request):
    """
        allows authenticated users to create a new event
        renders form on GET; saves event on valid POST
    """
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
    """
        handles new user registration
        logs the user in immediately after successful sign-up
    """
    if request.user.is_authenticated:
        return redirect(reverse('glasgowgaffsapp:index'))

    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)  # Hash the password
            user.save()
            registered = True

            login(request, user)

            return redirect(reverse('glasgowgaffsapp:index'))

        else:
            print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request, 'glasgowgaffsapp/register.html', context={'user_form': user_form, 'registered': registered})


def user_login(request):
    """
        handles user login
        redirects to homepage if credentials are valid
    """
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
    """
        logs out the current user and redirects to homepage
    """
    logout(request)
    return redirect(reverse('glasgowgaffsapp:index'))


def contact_us(request):
    """
        sends an email with user-entered contact info to the app owner
        called via a POST form submission
    """
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        subject = f"From {email}"
        body = f"""
        Name: {name}
    
    
        Message:{message}"""

        send_mail(
            subject,
            body,
            f"{email}",
            ["glasgowgaffs@gmail.com"],
            fail_silently=False,
        )

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def events(request):
    """
        displays a list of all events
    """
    all_events = Event.objects.all()
    return render(request, 'glasgowgaffsapp/events.html', {'events': all_events})


def event(request, event_id):
    """
        displays detailed information for a single event
    """
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'glasgowgaffsapp/event.html', {'event': event})


@login_required
def myevents(request):
    """
        shows events the user has created and ones they are attending
    """
    created_events = Event.objects.filter(created_by=request.user)
    attending_events = Event.objects.filter(attendees=request.user)

    return render(request, 'glasgowgaffsapp/myevents.html', {
        'created_events': created_events,
        'attending_events': attending_events
    })


@login_required
def toggle_attendance(request, event_id):
    """
        toggles attendance for the current user on a given event
        redirects back to the event page
    """
    event = get_object_or_404(Event, id=event_id)
    if request.user in event.attendees.all():
        event.attendees.remove(request.user)
    else:
        event.attendees.add(request.user)
    return redirect('glasgowgaffsapp:event', event_id=event.id)
