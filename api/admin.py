from django.contrib import admin
from .models import RenderVideo


class RenderVideoAdmin(admin.ModelAdmin):
    readonly_fields = ('pub_date',)
    list_display = ('id', 'text')
    search_fields = ('id', 'text', 'video')


admin.site.register(RenderVideo, RenderVideoAdmin)
