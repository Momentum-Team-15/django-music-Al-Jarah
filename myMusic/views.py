from django.shortcuts import render
from .models import Album


# Create your views here.
def index(request):
    return render(request, 'myMusic/index.html')


def album_detail(request, pk):
    album = Album.objects.get(pk=pk)
    return render(request, 'music/album_detail.html', {'album': album})
