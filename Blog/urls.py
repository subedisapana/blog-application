from . import views
from django.urls import path
from .views import (PostCreateView, PostUpdateView, PostDeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin




urlpatterns = [
    #
    path('', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='blogon_extend'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

]