from django.shortcuts import render, redirect
from .forms import VideoForm
from .models import Video


# функция рендеринга главной страницы
def index(request):
    latest = Video.objects.order_by('-pub_date')[:10]
    return render(request, 'index.html', {'videos': latest})


# функция загрузки видео через GUI
def new_video(request):
    form = VideoForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        video = form.save()
        video.save()
        return redirect('index')
    return render(request, 'new_video.html', {'form': form})
