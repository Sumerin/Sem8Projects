from django.shortcuts import render, redirect
from .models import News, Comment
from .forms import CommentForm
from django.contrib import messages

from django.http import HttpResponse


# Create your views here.
def index(request):
    context = {
        'news': News.objects.all()
    }
    return render(request, 'polls/index.html', context=context)


def about(request):
    return render(request, 'polls/about.html')


def news(request, id):
    if request.method == 'GET':
            context = {
                'news': News.objects.filter(id=id)[0],
                'comments': Comment.objects.filter(news=id),
                'form': CommentForm()
            }
            return render(request, 'polls/news.html', context)
    elif request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Skomentowałeś artykuł.")
            return redirect(request.path)

    return redirect('index')
