from django.shortcuts import render, HttpResponse, redirect
#from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import pyodbc
from . import models

conn = pyodbc.connect('Driver={Sql Server};'
                      'Server=DESKTOP-MH2HBH0\SQLEXPRESS01;'
                      'Database=student;'
                      'Trusted_Connection=yes;')
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render(request, 'index.html')


def SignupPage(request):
    if request.method == 'POST':
        iv = models.Student()
        iv.uname = request.POST.get('uname')
        iv.email = request.POST.get('email')
        iv.pass1 = request.POST.get('pass1')
        iv.pass2 = request.POST.get('pass2')

        if None in [iv.uname, iv.email, iv.pass1, iv.pass2]:
            return HttpResponse("Invalid form data. Please fill in all the fields.")

        if iv.pass1 != iv.pass2:
            return HttpResponse("Your password and confirm password do not match!")
        else:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO stdlogin VALUES (?, ?, ?, ?)", (iv.uname, iv.email, iv.pass1, iv.pass2))
            conn.commit()
            return redirect('login')

    return render(request, 'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass1')

        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM stdlogin WHERE uname = ? AND pass1 = ?", (username, password))
        result = cursor.fetchone()

        if result[0] == 1:
            return HttpResponse("<center><h1>You are logged in to the device</h1></center>") # Redirect to home page or any other desired page
        else:
            return HttpResponse("Invalid username or password!")

    return render(request, 'login.html')
def LogoutPage(request):
    logout(request)
    return redirect('login')

