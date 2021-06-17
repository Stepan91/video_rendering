from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_video, name='upload_video'),
    path('render/', views.render_video, name='render_video'),
    path('render/<int:render_id>/', views.render_view, name='render_view')
]
