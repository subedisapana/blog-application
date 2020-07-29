from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Post
from .form import BlogForm
from .form import SignUpForm, ProfileUpdateForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.decorators import login_required
# from django. core.mail import send_mail


def homepage(request):
    return render(request, 'homepage.html')


@login_required
def blog(request):
    return request(request, 'blog.html')


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now login.')
            return redirect('login')
    else:
            form = SignUpForm()
    return render(request, 'auth/signup.html', {'form': form})


def login_view(request):
    return render(request, 'auth/login.html')


def logout_view(request):
    return render(request, 'auth/logout.html')


def profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if p_form.is_valid():

            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'p_form': p_form
        }
        return render(request, 'user/profile.html', context)


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
        form = BlogForm()    # form ob created. and is passed to template
        return render(request, 'create.html', {'form': form})
    else:
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            print("after validation on views", form.cleaned_data) # Data in clean data
            return redirect('/blog')
        else:
            return HttpResponse(request, 'create.html', {'form': form})


# ---------------------------------------------------------------------------------------------------------------

#def blog(request):
#    subject = "Test"
#    message = "You have successfully logged in!!"
#    from_email = "sapana@gmail.com"
#   recipient = [request.user.email]
#   send_mail(subject, message, from_email, recipient)
#   return render(request, 'blog.html')


