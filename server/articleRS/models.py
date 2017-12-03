from django.db import models

import datetime

class Article(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=20)
    date_publi = models.DateTimeField('date published')

    def __str__(self):
        return "titre : " + self.titre

class Composant(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    positon = models.IntegerField()
    type = models.IntegerField()
    data = models.TextField()

    def __str__(self):
        return "type : " + self.type + ", article : " + self.article

