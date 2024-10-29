from . import views
from django.urls import path , include

urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('viewbook/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/text/formatting', views.format, name="books.format"),
    path('html5/listing', views.listing, name="books.listing"),
    path('html5/links', views.link, name= "books.link"),
    path('html5/tables', views.tables, name= "books.tables"),
    path('search/', views.search, name= "books.search"),
    path('simple/query/', views.simple_query, name= "books.simple_query"),
    path('complex/query/', views.lookup_query, name= "books.lookup_query"),
]
