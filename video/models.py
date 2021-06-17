from django.db import models


class Video(models.Model):
    description = models.CharField(max_length=200, verbose_name='Описание')
    video = models.FileField(
        upload_to='uploads/videos/%Y/%m/%d/',
        verbose_name='Видео'
    )
    background = models.ImageField(
        upload_to='uploads/images/%Y/%m/%d/',
        verbose_name='Фоновое фото',
        blank=True
    )
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
