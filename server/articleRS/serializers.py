from articleRS.models import Article, Composant
from rest_framework import serializers

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('titre', 'auteur', 'date_publi')

class ComposantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Composant
        fields = ('article', 'positon', 'type', 'data')