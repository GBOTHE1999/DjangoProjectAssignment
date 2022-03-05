from django.shortcuts import render
from .models import Post 
from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm,PostForm
from django.contrib.auth.forms import  UserCreationForm 
from django.views.generic import  CreateView 

def Dashboard(request):
    return render(request,  'User/dashboard.html')

def PostListView(request):
    post_menu_list = Post.objects.all()
    return render(request, 'User/PostView.html', {'post_menu_list': post_menu_list})

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name ='registration/register.html'
    success_url = reverse_lazy('login')

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'user/add_post.html'