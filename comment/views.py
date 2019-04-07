from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from .models import Comment

# Create your views here.
def index(request):
    return render(request, 'comment/all.html', {
        'comments': Comment.objects.all()
    })

def add_comment(request):
    comment = Comment(
        comment=request.POST['comment']
    )
    comment.save()

    return HttpResponseRedirect('/')
