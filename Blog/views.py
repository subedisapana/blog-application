from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Post
from .form import BlogForm
from .form import SignUpForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.decorators import login_required


def homepage(request):
    return render(request, 'homepage.html')


@login_required
def blog(request):
    return request(request, 'blog.html')


def signup_view(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'You have successfully registered your account:' + user)
            #login(request, user)
            return redirect('login_view')
    #else:
        #form = SignUpForm()
    #return render(request, 'auth/signup.html', {'form': form})

    context = {'form': form}
    return render(request, 'auth/signup.html', context)


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password1 = request.POST.get('password1')

        user = authenticate(request, username=username, password=password1)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.info(request, "sorry")


    context = {}
    return render(request, 'auth/login.html', context)

    #if request.method == "POST":
       # username = request.POST.get("username")
       # password = request.POST.get("password")
       # print(username)
        #user = authenticate(request, username=username, password=password)
        #if user is not None:
           # login(request, user)
          #  return redirect('homepage')
    #context = {}
    #return render(request, 'auth/login.html', context)








# -------------------------------------blog view--------------------------------------------------------


class PostList(generic.ListView):
    queryset = Post.objects.filter(status='Published').order_by('-created')
    template_name = 'blog.html'
    model = Post
    context_object_name = 'post_list'
    paginate_by = 2
    ordering = ['-created']


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blogon_extend.html'


def blog_form(request):
    if request.method == 'GET':
        form = BlogForm()    # obj create, aba yo obj lai template ma pass garni
        return render(request, 'create.html', {'form': form})
    else:
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            print("after validation on views", form.cleaned_data) # clean_data vanni attribute ma aayera bascha
            return HttpResponse("Saved Sucessfully!!")
        else:
            return HttpResponse(request, 'create.html', {'form': form})


