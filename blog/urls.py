from django.urls import path
from .views import ( 
	IndexPage,
	ContactPage,
	CategoryPage,
	AboutPage,
	AllArticleAPIView,
	SingleArticleAPIView,
	SearchArticleAPIView,
	SubmitArticleAPIView,
 )

urlpatterns = [
	path('', IndexPage.as_view(), name='index'),
	path('contact/', ContactPage.as_view(), name='contact'),
	path('category/', CategoryPage.as_view(), name='category'),
	path('about/', AboutPage.as_view(), name='about'),
	path('article/', SingleArticleAPIView.as_view(), name='single_article'),
	path('article/all/', AllArticleAPIView.as_view(), name='article_all'),
	path('article/search/', SearchArticleAPIView.as_view(), name='article-search'),
	path('article/submit/', SubmitArticleAPIView.as_view(), name="article-submit"),	
]