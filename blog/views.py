from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

posts = [{"author": "Ojim",
          "title":"Money is Good",
          "content":"Having money save you from shege",
          "date_posted": "January, 2024"},
         {"author": "Smario",
          "title":"God Loves you",
          "content":"For God so love the world that he gave his only begotten son",
          "date_posted": "feb, 2024"
          }]


def home(request):

    context = { "posts": Post.objects.all()

    }
    return render(request, 'blog/home.html',context)


def about(request):
    return render(request, 'blog/about.html', {'title':"About"})