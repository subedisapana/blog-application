from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Post
from .form import BlogForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)


def homepage(request):
    return render(request, 'homepage.html',)

# -------blog view--------------------------------------------------


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


