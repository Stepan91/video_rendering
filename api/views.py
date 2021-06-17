from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from .serializers import CreateVideoSerializer, RenderVideoSerializer
from .models import RenderVideo
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse
from moviepy.editor import *


# функция загрузки видео по API
@api_view(['POST'])
def upload_video(request):
    description = request.data['description']
    video = request.data['video']
    background = request.data['background']
    data = {
        'description': description,
        'video': video,
        'background': background
    }
    serializer = CreateVideoSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)


# функция рендеринга загруженного видео
@api_view(['POST'])
def render_video(request):
    text = request.data['text']
    video = request.data['video']
    # из загруженного видео делаем вырезаем с 20-й по 30-ю секунду
    clip = VideoFileClip(
        'media/uploads/videos/2021/06/18/videoplayback1.mp4'
        ).subclip(20, 30)
    # уменьшаем громкость до 0.8 от первоначальной
    clip = clip.volumex(0.8)
    # задаём текст
    txt_clip = TextClip(text, fontsize=70, color='white')
    txt_clip = txt_clip.set_pos('center').set_duration(10)
    # задаём фон
    bg = ImageClip('media/uploads/images/2021/06/18/cat1.jpg').set_duration(5)
    # рендерим изменения в новое видео
    new_video = CompositeVideoClip([clip, txt_clip, bg])
    # записываем полученное видео в новый файл
    new_video.write_videofile(f'edited_{text}.mp4')
    data = {
        'text': text,
        'video': video,
        'background': bg,
        'new_video': new_video
    }
    serializer = RenderVideoSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def render_view(request, render_id):
    rendered = get_object_or_404(RenderVideo, id=render_id)
    if rendered:
        return HttpResponse(rendered)
    raise FileNotFoundError
