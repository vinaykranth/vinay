from django.contrib.sites import requests
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import render
import random
import string
import requests
from django.template.defaulttags import comment

from . import forms
from .forms import IntegerDateForm, PieChartForm, FeedbackForm
from .models import Register


# Create your views here.

def hello(request):
    return HttpResponse("<center>Welcome To TTM HomePage</center>")


def NewHomePage(request):
    return render(request, 'NewHomePage.html')


def Travel(request):
    return render(request, 'Travel.html')


def print1(request):
    return render(request, 'print_to_console.html')


def print_to_console(request):
    user_input = ''  # Initialize user_input for the case of a GET request
    if request.method == "POST":
        user_input = request.POST.get('user_input', '')  # Use get() to avoid UnboundLocalError
        print(f"User Input: {user_input}")
        # return HttpResponse('Form submitted successfully')
    a1 = {'user_input': user_input}
    return render(request, 'print_to_console.html', a1)


def randomcall(request):
    return render(request, 'randomoptgenerator.html')


def randomcall1(request):
    if request.method == "POST":
        user_input = request.POST.get('user_input')
        print(f'user input:{user_input}')
        a2 = int(user_input)
        ran1 = ''.join(random.sample(string.digits, k=a2))
    a1 = {'ran1': ran1}
    return render(request, 'randomoptgenerator.html', a1)


def getdate1(request):
    return render(request, 'DateTime.html')


import datetime
from django.shortcuts import render


def get_date(request):
    if request.method == 'POST':
        form = IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value = form.cleaned_data['integer_value']
            date_value = form.cleaned_data['date_value']
            updated_date = date_value + datetime.timedelta(days=integer_value)
            return render(request, 'DateTime.html', {'updated_date': updated_date})
        else:
            form = IntegerDateForm()
        return render(request, 'DateTime.html', {'form': form})


def registerloginfunction(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phonenumber = request.POST.get('phonenumber')
        if Register.objects.filter(email=email).exists():
            return HttpResponse("Email already registered.Choose a different email.")
        Register.objects.create(name=name, email=email, password=password, phonenumber=phonenumber)
        return redirect('NewHomePage')
    return render(request, 'Register.html')


def registerlogin(request):
    return render(request, 'Register.html')


import matplotlib.pyplot as plt
import numpy as np


def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart image
            img1 = {'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'chart_form.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'chart_form.html', {'form': form})


def PieChartForm1(request):
    return render(request, 'chart_form.html')


def car(request):
    return render(request, 'car.html')


def weatherpagecall(request):
    return render(request, 'weatherappinput.html')


from django.shortcuts import render, redirect
from .models import Feedback
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback
from django.contrib import messages

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import FeedbackForm
from .models import Feedback

def feedbackfunction(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phonenumber = form.cleaned_data['phonenumber']
            comments = form.cleaned_data['comments']
            tosend = comments + '_this is copy'

            # Save feedback data to the database
            feedback = Feedback(name=name, email=email, phonenumber=phonenumber, comments=comments)
            feedback.save()

            # Sending email
            send_mail(
                'Thank You',
                tosend,
                '2200030924cseh@gmailcom',
                [email],
                fail_silently=False,
            )

            # Display a success message
            messages.success(request, 'Feedback submitted successfully.')

            return redirect('/')  # Change 'thank_you_page' to the actual URL or name of your thank you page

    else:
        form = FeedbackForm()  # create an instance of the form for GET requests

    return render(request, 'contactus.html', {'form': form})


def feedback(request):
    return render(request, 'contactus.html')

def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = '5a49c72db247352450eb15b55f1f5974'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1 = round(temperature - 273.15, 2)
            return render(request, 'weatherappinput.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weatherappinput.html', {'error_message': error_message})


from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login(request):
    return render(request, 'login.html')


def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        user = auth.authenticate(username=username, password=pass1)
        if user is not None:
            auth.login(request, user)
            return render(request, 'user_page.html', {'user': user})
        else:
            messages.info(request, 'Invalid credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def signup1(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken')
                return render(request, 'signup.html')
            else:
                user = User.objects.create_user(username=username, password=pass1)
                user.save()
                messages.info(request, 'Account created successfully!!')
                return render(request, 'login.html')
        else:
            messages.info(request, 'Password do not match')
            return render(request, 'signup.html')


def logout(request):
    auth.logout(request)
    return render(request, 'NewHomepage.html')
