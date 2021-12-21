from django.contrib import messages
from django.db.models import query
from django.http.request import HttpRequest
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *
from .forms import addBook

# Create your views here.
def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        my_user = User.objects.create_user(username, email, password)
        my_user.first_name = name
        my_user.save()

    return render(request, 'signup.html')

# Function to sign in the page.
def signin(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            password = request.POST.get('password')

            # Have used default django login system.
            print(name, password)
            user = authenticate(username=name, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home')
        return render(request, 'login.html')

def home(request):
    allBooks = Books.objects.all()
    context = {'allBooks':allBooks}
    return render(request, 'home.html', context)

# Function to sign out from the page.
def signout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/signin')
    return render(request, 'login.html')

def add_book(request):
    form = addBook()
    if request.method == 'POST':
        form = addBook(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/home')
    context = {'form':form}
    return render(request, 'addBook.html', context)

def search(request):
    query_name = request.GET["query"]

    if len(query_name) > 50:
        search_results = []
    else:
        search_Category = Books.objects.filter(book_category__contains=query_name)
        search_Books = Books.objects.filter(book_name__icontains=query_name)
        search_results = search_Books.union(search_Category)

    context = {"search_Books" : search_results, "query":query_name}
    return render(request, 'search.html', context)
