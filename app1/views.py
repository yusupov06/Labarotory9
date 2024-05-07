from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Content
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import render

class Post_view(ListView):
    model = Content
    template_name = 'homepage.html'

class Post_detail(DetailView):
    model = Content
    template_name='about.html'
    context_object_name = 'post'

class Create_post(CreateView):
    model = Content
    template_name = 'createpage.html'
    fields = ['title', 'text', 'author']

class Edit_post(UpdateView):
    model = Content
    template_name = 'createpage.html'
    fields = ['title', 'text', 'author']

class Delete_post(DeleteView):
    model = Content
    template_name = 'deletepage.html'
    success_url = reverse_lazy('Post_view')

def Logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html')