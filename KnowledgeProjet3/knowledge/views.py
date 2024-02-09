from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, View
from knowledge.Forms import ArticleForm, CategoryForm
from knowledge.models import Article, Category

#Classe pour la page d'accueil
class IndexView(TemplateView):
    template_name = 'knowledge/index.html'

#Classe pour la page de monitoring
class MonitoringView(TemplateView):
    template_name = 'knowledge/monitoring.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorie_nom'] = 'LeNomDeCategorie'
        return context

#Classe qui permet d'afficher la liste des catégories parents
class CategoryParentView(View):
    template_name = 'knowledge/category.html'

    def get(self, request, *args, **kwargs):
        category_name = kwargs.get('category_name')
        categories = Category.objects.filter(parent__isnull=True)
        return render(request, self.template_name, {'category_name': category_name, 'categories': categories})

#Classe qui permet d'afficher la liste des catégories enfants
class CategoryChildView(View):
    template_name = 'knowledge/child_category.html'

    def get(self, request, category_id):
        parent_category = get_object_or_404(Category, id=category_id)
        child_categories = parent_category.children.all()
        return render(request, self.template_name, {'parent_category': parent_category, 'child_categories': child_categories})
    
#Classe qui permet de créer des OSs
class CreateCategorieView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'knowledge/create_category.html'
    success_url = '/category/'
    def get(self, request):
        form = CategoryForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CategoryForm(request.POST)

        if form.is_valid():
            category = form.save()
            return redirect('category')

        return render(request, self.template_name, {'form': form})

#Classe pour la page des articles
class ArticleDetailView(View):
    template_name = 'knowledge/article.html'

    def get(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        parent_category = article.category.parent if article.category.parent else None
        update_url = reverse('article', kwargs={'article_id': article.id})
        return render(request, self.template_name, {'article': article, 'update_url': update_url})
    
#Classe pour la création des articles
class CreateArticleView(CreateView):
    template_name = 'knowledge/create_article.html'
    form_class = ArticleForm

    def get(self, request, category_id):
        form = self.form_class(initial={'category': category_id})
        return render(request, self.template_name, {'form': form, 'category_id': category_id})

    def post(self, request, category_id):
        form = self.form_class(request.POST)

        if form.is_valid():
            article = form.save(commit=False)
            article.category_id = category_id
            article.save()
            return redirect('article', article_id=article.id) 

        return render(request, self.template_name, {'form': form, 'category_id': category_id})
