from django.shortcuts import render, redirect
from .models import Post
# Create your views here.

def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })



def post(request):
    if request.method == 'POST':
        post = Post()
        post.text = request.POST['text']
        post.save()
        return redirect('post')
    else:
        post = Post.objects.all()
        return render(request, 'post_list.html', {'post':post})
