from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import login, logout,authenticate
from .forms import CustomerVerificationForm

from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request,'home.html')  # Adjust 'home' to the name of your home page URL
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')
def logout_view(request):
    logout(request)
    return redirect('login')
def home(request):
    return render(request, 'home.html')

def survey_create(request):
    if request.method == 'POST':
        survey_title = request.POST.get('surveyTitle')
        questions = request.POST.getlist('question[]')

        # Process the survey data here, such as saving it to a database.

        return render(request, 'survey.html', {'survey_title': survey_title})

    return render(request, 'survey.html')
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def signup(request):
    if request.method == 'POST':
        # Use Django's built-in UserCreationForm for simplicity
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after successful signup
            login(request, user)
            # Redirect to the home page (adjust the URL as needed)
            return redirect('home')

    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})



def survey_types(request):
    # Your logic to get survey types and counts goes here
    survey_types_data = [
        ('Customers', 45),
        ('Education', 24),
        ('Employees', 76),
        ('Events', 11),
        ('Forms', 68),
        ('Healthcare', 24),
        ('Market Research', 60),
        ('Nonprofit', 5),
        ('Other', 51),
    ]

    return render(request, 'recentsurveys.html', {'survey_types_data': survey_types_data})


def customersurvey(request):
    if request.method == 'POST':
        form = CustomerVerificationForm(request.POST)
        if form.is_valid():
            # Process the verification data (store in database, etc.)
            # Redirect to a success page or perform further actions
            return HttpResponse("Verification Successful!")
    else:
        form = CustomerVerificationForm()

    return render(request, 'customersurvey.html', {'form': form})

from .forms import FeedbackForm

def websitefeedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Process the feedback (e.g., save to database)
            # Redirect to a thank you page or display a success message
            return HttpResponse("Thank you for your feedback!")
    else:
        form = FeedbackForm()
    return render(request, 'websitefeedback.html', {'form': form})