from django.conf.urls import url

from . import views


urlpatterns = [
 url(r'^$', views.index, name='index'),
 url(r'^books/$', views.BookListView.as_view(), name='books'),
 url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
 url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),  
 url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [   
    url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]