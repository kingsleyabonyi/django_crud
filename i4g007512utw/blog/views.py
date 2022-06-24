from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.edit import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


from blog.models import Post

# Create your views here.

class PostListView(ListView):
    #To specify the model for the list view
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields =  "__all__"
    success_url = reverse_lazy("blog:all")

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDeleteView(DeleteView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
