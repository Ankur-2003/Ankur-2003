from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate
from .models import *

# Create your views here.
def signup(request):
    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')

        # Have used default django login system.
        user = authenticate(username=name, password=password)
        if user is not None:
            allBooks = Books.objects.all()
            print(allBooks)
            context = {'allBooks':allBooks}
            return render(request, 'home.html', context)

    return render(request, 'login.html')