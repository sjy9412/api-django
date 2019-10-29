from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Music, Artist, Review
from .serializers import MusicSerializers
# Create your views here.

@api_view(['GET']) # HTTP method
def index(request):
    musics = Music.objects.all()
    serializer = MusicSerializers(musics, many=True) # Queryset이라 may option이 필요
    return Response(serializer.data)

@api_view(['GET'])
def detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    serializer = MusicSerializers(music) # 단일 데이터라 many 필요 없음
    return Response(serializer.data)