from django.shortcuts import render

from core.models import Post, Tag


def home(request):
    context = {
        'posts': Post.objects.all(),
        'tags': Tag.objects.all(),
    }

    return render(request, "blog/home.html", context)




