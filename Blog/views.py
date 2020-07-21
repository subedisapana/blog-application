from django.shortcuts import render
from django.views import generic
from .models import Post


def homepage(request):
    return render(request, 'homepage.html',)


def create(request):
    return render(request, 'create.html', )


class PostList(generic.ListView):
    queryset = Post.objects.filter(status='Published').order_by('-created')
    template_name = 'blog.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blogon_extend.html'

