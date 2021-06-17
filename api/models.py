from django.db import models
from video.models import Video


class RenderVideo(models.Model):
    text = models.CharField(max_length=200, verbose_name='Описание')
    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
        related_name='rendervideo',
        verbose_name='Видео первоначальное'
        )
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Рендер'
        verbose_name_plural = 'Рендеры'
