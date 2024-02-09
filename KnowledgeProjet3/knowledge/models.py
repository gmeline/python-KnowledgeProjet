from django.db import models
from django.urls import reverse
from tinymce import models as tinymce_models

#Modèle pour les catégories
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    parent = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)#Model pour mettre des parents ou non
    def __str__(self):
        return self.titre
    
    @property
    def children(self):
        return Category.objects.filter(parent=self)

#Modèle pour les articles
class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="articles")
    titre = models.CharField(max_length=100)
    presentation = models.CharField(max_length=250)
    contenu = models.TextField()
    date_publication = models.IntegerField(default=11)
    

    def __str__(self):
        return self.titre

