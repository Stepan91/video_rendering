from django.contrib import admin
from .models import Video


class VideoAdmin(admin.ModelAdmin):
    readonly_fields = ('pub_date',)
    list_display = ('id', 'description')
    search_fields = ('id', 'description')


admin.site.register(Video, VideoAdmin)
