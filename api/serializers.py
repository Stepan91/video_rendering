from rest_framework import serializers
from .models import RenderVideo
from video.models import Video


class CreateVideoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'description', 'background', 'video')
        model = Video


class RenderVideoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'text', 'video')
        model = RenderVideo
