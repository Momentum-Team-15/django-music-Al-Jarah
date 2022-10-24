from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from .forms import AlbumForm


# Create your views here.
def index(request):
    albums = Album.objects.all()
    return render(request, 'myMusic/index.html', {'albums': albums})


def album_detail(request, pk):
    album = Album.objects.get(pk=pk)
    return render(request, 'myMusic/album_detail.html', {'album': album})


def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album=form.save()
            return redirect("home")
    else:
        form = AlbumForm()
    return render(request, 'myMusic/create_album.html', {'form': form})


def album_edit(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            # album = form.save(commit=False)
            album = form.save()
            return redirect('album_detail', pk=album.pk)
    else:
        form = AlbumForm(instance=Album)
    return render(request, 'myMusic/album_edit.html', {'form': form})

