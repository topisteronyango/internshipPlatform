from django.shortcuts import render
from django.views import generic
from .models import BlogPost

# Create your views here.

class PostList(generic.ListView):
    queryset = BlogPost.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'


    # new code
    # blogs = BlogPost.objects.all()
    # myfilter = JobFilter(request.GET, queryset=blogs)
    # blogs = myfilter.qs # qs 
    # template_name = 'blog.html'

class PostDetail(generic.DetailView):
    model = BlogPost
    template_name = 'blog_post_detail.html'
