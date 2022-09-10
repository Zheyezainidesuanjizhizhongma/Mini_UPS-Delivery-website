from ctypes.wintypes import DOUBLE
from itertools import product
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
from ups_front.models import CreatedUsersForm, Truck_info, Package_info, Product_info, Feedback_info
from django.http import HttpResponse
from django.core.mail import send_mail
import socket
import sys
import time

# Create your views here.
posts = [
    {
        'author': 'UPS',
        'title': 'Welcome to UPS',
        'content': 'Hi there!',
        'date_posted': 'Since 1907'
    },
]


def loginUsers(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("ups-home")
    else:
        form = AuthenticationForm()
    return render(request, 'ups_front/login.html', {'form': form})


def signupUsers(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = CreatedUsersForm(request.POST)
        if form.is_valid():
            form.save()
            form.cleaned_data.get('username')
            messages.success(request, 'Account created successfully!')
            return redirect("loginusers")
    else:
        form = CreatedUsersForm()
    return render(request, "ups_front/sign_up.html", {'form': form})


# def sendUserID(user_id):
#     # time.sleep(2)
#     try:
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         s.connect(('127.0.0.1', 34561))
#         print("success: connect to back end")
#         print('==========user_id: ', user_id)
#         user_id = str(user_id)
#         s.send(user_id.encode('utf-8'))
#     except socket.error as error_msg:
#         print(error_msg)
#         sys.exit(1)


def home(request):
    # send the user id to back end
    request.session.get('_auth_user_id')
    # sendUserID(user_id)
    context = {'posts': posts}
    return render(request, 'ups_front/home.html', context)


def profile(request):
    try:
        owner_id = request.session.get('_auth_user_id')
        u = User.objects.get(id=owner_id)
        username = u.username
        email = u.email
        user_info = {'username': username, 'email': email}
        return render(request, 'ups_front/profile.html', user_info)
    except:
        print('')
    return render(request, 'ups_front/home.html')


def packageList(request):  # package list
    try:
        owner_id = request.session.get('_auth_user_id')
        package = Package_info.objects.filter(user_id=owner_id)
        if package:
            context = {"packages": package}
            return render(request, "ups_front/package_info.html", context)
        else:
            messages.success(request, "You have no package currently")
            return render(request, 'ups_front/home.html')
    except:
        messages.error(request, "Load the package list unsuccessfully...")
        return render(request, 'ups_front/home.html')


def onepackage(request):
    try:
        packageid = request.POST['package']
        package = Package_info.objects.get(package_id=packageid)
        product = Product_info.objects.filter(package_id=packageid)

        context = {'package': package, 'product': product}
        return render(request, 'ups_front/onepackage.html', context)
    except:
        messages.error(request, "Pacakge info has some problem...")
        return render(request, 'ups_front/home.html')


def searchPackage(request):
    return render(request, 'ups_front/search.html')


def searchResult(request):
    try:
        pck_id = request.POST['package_id']
        package = Package_info.objects.get(package_id=pck_id)
        product = Product_info.objects.filter(package_id=pck_id)
        context = {'package': package, 'product': product}
        if package:
            return render(request, 'ups_front/onepackage.html', context)
        else:
            messages.error(request, "Tracking number does not exist...")
            return render(request, 'ups_front/home.html')
    except:
        messages.error(request, "Can't find package information...")
        return render(request, 'ups_front/home.html')


def feedback(request):
    return render(request, "ups_front/feedback.html")


def submitFeedback(request):
    try:
        owner_id = request.session.get('_auth_user_id')
        feedback_ob = Feedback_info()
        feedback_ob.user_id = int(owner_id)
        feedback_ob.grade = int(request.POST['grade'])
        feedback_ob.text = request.POST['feedback_text']
        feedback_ob.save()
        messages.success(request, "You have submitted feedback successfully")
        return render(request, 'ups_front/feedback_history.html')
    except:
        messages.error(request, "Submit feedback unsuccessfully...")
        return render(request, 'ups_front/home.html')


def viewFeedback(request):
    try:
        owner_id = request.session.get('_auth_user_id')
        feedbacks = Feedback_info.objects.filter(user_id=owner_id)
        context = {"feedbacks": feedbacks}
        return render(request, "ups_front/view_feedback.html", context)
    except:
        messages.error(request, "View feedback unsuccessfully...")
        return render(request, 'ups_front/home.html')


def update(request):
    try:
        pck_id = request.POST['pck_id']
        package = Package_info.objects.get(package_id=pck_id)
        print('----------------x:', package.destination_x)
        print('----------------y:', package.destination_y)
        package.destination_x = request.POST['destination']
        package.destination_y = request.POST['add_destination']
        package.save()
        owner_id = request.session.get('_auth_user_id')
        owner = User.objects.get(id=owner_id)
        owner_email = owner.email
        myEmail = 'The destination address of your package ' + str(package.package_id) + ' has been changed to (' + str(package.destination_x) + ', ' + str(package.destination_y) + ').'
        send_mail('New message from UPS', myEmail, from_email = 'ece568_no_reply@outlook.com', recipient_list = [owner_email], fail_silently=False)
        messages.success(request, "Information updated successfully! You should have received a confirmation email.")
    except:
        messages.error(request, "Try it again...")
    return render(request, "ups_front/home.html")


def trackpackage(request):
    return render(request, 'ups_front/tracking.html')


def trackResult(request):
    try:
        pck_id = request.POST['package_id']
        print('zzzzzzzzzzzzzzzzzpck_id: ', pck_id)
        package = Package_info.objects.get(package_id=pck_id)
        context = {'package': package}
        if package:
            messages.success(request, "For more information, please log in...")
            return render(request, 'ups_front/track_package.html', context)
    except:
        messages.error(request, "Can't find package information...")
    return render(request, 'ups_front/tracking.html')

def calculate(request):
    weight = request.POST["weight"]
    distance = request.POST["distance"]
    weight_int = float(weight)
    distance_int = float(distance)
    cost_string = 'Your cost is ' + str(weight_int * distance_int) + '$'
    messages.success(request, cost_string)
    return render(request, 'ups_front/cost.html')


def cost(request):
    return render(request, 'ups_front/cost.html')


