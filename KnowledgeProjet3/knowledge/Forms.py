from django import forms

from tinymce.widgets import TinyMCE
from .models import Category, Article

#Form pour les catégories
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['titre','description','parent']

#Form pour les articles
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['category', 'titre', 'presentation','contenu']
        widgets = {
            'contenu': TinyMCE(attrs={'cols': 80, 'rows': 30}),
        }
