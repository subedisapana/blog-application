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
    context = {}
    form = SignUpForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request , user)
            return render(request, 'blog.html')
    context['form'] = form
    return render(request, 'auth/signup.html', context)

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


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'create.html'
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    template_name = 'post_delete.html'
    success_url = '/blog'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def blog_form(request):
    if request.method == 'GET':
        form = BlogForm()    # obj create, aba yo obj lai template ma pass garni
        return render(request, 'create.html', {'form': form})
    else:
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            print("after validation on views", form.cleaned_data) # clean_data vanni attribute ma aayera bascha
            return redirect('/blog')
        else:
            return HttpResponse(request, 'create.html', {'form': form})


