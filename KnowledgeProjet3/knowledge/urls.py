from django.urls import path
from knowledge.views import ArticleDetailView, CreateArticleView, CreateCategorieView, IndexView,CategoryParentView,MonitoringView, CategoryChildView

urlpatterns = [
    path('', IndexView.as_view(), name='accueil'),
    path('monitoring/', MonitoringView.as_view(), name='monitoring'),
    path('monitoring/', MonitoringView.as_view(), name='monitoring'),
    path('categorie/', CategoryParentView.as_view(), name='category'),
    path('categorie/<int:category_id>/', CategoryParentView.as_view(), name='category'),
    path('categorie/<int:category_id>/enfants/', CategoryChildView.as_view(), name='child_category'),
    path('create_category/', CreateCategorieView.as_view(), name='create_category'),
    path('categories/', CategoryParentView.as_view(), name='category'),
    path('article/<int:article_id>/', ArticleDetailView.as_view(), name='article'),
    path('create_article/<int:category_id>/', CreateArticleView.as_view(), name='create_article'),
]

