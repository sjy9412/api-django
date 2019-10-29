from django.urls import path
from . import views

urlpatterns = [
    path('musics/', views.index, name='music'),
    path('musics/<int:music_pk>/', views.detail, name='detail')
]
