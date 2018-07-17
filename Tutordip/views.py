from django.shortcuts import render , redirect , render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.files import File
from django.urls import resolve
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm
from Blogs.models import Blogs as blogs
from Blogs.models import Becometutor
from Blogs.models import Tutoradmin
from Blogs.models import Selectsubject
from Blogs.forms import blogform, becometutorform, tutoradmin, Selectsubjectform
from django import forms

def admin_dashboard(request):
    return render(request, 'dashboard.html')

def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                if user.is_superuser:
                    login(request,user)
                    return redirect('admin_dashboard')
                else:
                    login(request,user)
                    return redirect('home')
            else:
                return render(request, 'authentication/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'authentication/login.html', {'error_message': 'Invalid login'})
    return render(request, 'authentication/login.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'authentication/signup.html', {'form': form})


def index(request):
    a = request.GET.get('subject')
    if a:
        tutorlist = Tutoradmin.objects.filter(Subjects__contains=a)
        page = request.GET.get('page', 1)
        paginator = Paginator(tutorlist, 2)
        try:
            tutorlist = paginator.page(page)
        except PageNotAnInteger:
            tutorlist = paginator.page(1)
        except EmptyPage:
            tutorlist = paginator.page(paginator.num_pages)
        context = {'tutorlist': tutorlist, 'a':a}
        return render(request, 'tutor.html', context)
    else:
        form = Selectsubjectform()
        Blogs = blogs
        Bloglist = Blogs.objects.all()
        Bloglist = Bloglist.order_by('-id')[:3]
    return render(request, 'index.html', { 'form' : form , 'Bloglist':Bloglist})


def aboutus(request):
    return render(request, 'about.html')


def faq(request):
    return  render(request, 'faq.html')


def privacy(request):
    return  render(request, 'privacy.html')


def terms(request):
    return render(request, 'terms.html')


def register(request):
    return  render(request, 'register.html')

def logoutuser(request):
    logout(request)
    return redirect('home')

def becometutor(request):
    if request.method == "POST":
        form = becometutorform(request.POST, request.FILES)
        if form.is_valid():
            child = form.save(commit=False)
            child.save()
            return redirect('Blogs')
    else:
        form = blogform()
    return render(request, 'become-a-tutor.html', { 'form': form })

def pricing(request):
    return  render(request, 'pricing.html')

def Blogs(request):
    Blogs = blogs
    Bloglist = Blogs.objects.all()
    Bloglist = Bloglist.order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(Bloglist, 2)
    try:
        Blogs = paginator.page(page)
    except PageNotAnInteger:
        Blogs = paginator.page(1)
    except EmptyPage:
        Blogs = paginator.page(paginator.num_pages)
    context = {'Blogs': Blogs}
    return render(request, 'blog.html', context)

def add_blog(request):
    if request.method == "POST":
        form = blogform(request.POST, request.FILES)
        if form.is_valid():
            child = form.save(commit=False)
            child.save()
            return redirect('Blogs')
    else:
        form = blogform()
    return render(request,'addblog.html',{ 'form': form })

def blogid(request , id):
    Bloglist = blogs.objects.get(id=id)
    a = Bloglist
    context = {'a': a}
    return render(request, 'blog-detail.html', context)

def tutorrequests(request):
    becometutor = becometutorform.objects.all()
    becometutor = becometutor.order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(becometutor, 2)
    try:
        becometutor = paginator.page(page)
    except PageNotAnInteger:
        becometutor = paginator.page(1)
    except EmptyPage:
        becometutor = paginator.page(paginator.num_pages)
    context = {'becometutor': becometutor}
    return render(request, 'blog.html', context)

def deletetutorrequest(request, id):
    album = Becometutor.objects.get(id=id)
    album.delete()
    return redirect('tutorrequests')

def tutor(request):
    tutorlist = Tutoradmin.objects.all()
    tutorlist = tutorlist.order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(tutorlist, 2)
    try:
        tutorlist = paginator.page(page)
    except PageNotAnInteger:
        tutorlist = paginator.page(1)
    except EmptyPage:
        tutorlist = paginator.page(paginator.num_pages)
    context = {'tutorlist': tutorlist}
    return render(request, 'tutor.html', context)

def tutorprofile(request, id):
    profile = Tutoradmin.objects.get(id=id)
    a = profile
    context = {'a': a}
    return render(request, 'tutor-profile.html', context)

def tutorformadmin(request):
    if request.method == "POST":
        form = tutoradmin(request.POST, request.FILES)
        if form.is_valid():
            child = form.save(commit=False)
            child.save()
            return redirect('Blogs')
    else:
        form = tutoradmin()
    return render(request, 'tutoradmin.html',{ 'form': form })

def studenthistory(request):
    return render(request, 'student-history.html')