from django.shortcuts import render
from django.views import generic
from .models import Post
from .models import Tag

class PostList(generic.ListView):
    queryset = Post.objects.all().order_by('-created_on')
    template_name = 'index.html'

class TagList(generic.ListView):
    queryset = Tag.objects.all()
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
