from django.shortcuts import render
from articleRS.models import Article, Composant
from rest_framework import viewsets
from articleRS.serializers import ArticleSerializer, ComposantSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ComposantViewSet(viewsets.ModelViewSet):
    queryset = Composant.objects.all()
    serializer_class = ComposantSerializer