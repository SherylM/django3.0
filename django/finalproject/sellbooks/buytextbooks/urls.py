from django.conf.urls import url
from . import views

app_name = "books"

urlpatterns = [

    #/buytextbooks/
    url(r'^$', views.home, name='home'), #views.index,name = 'index'

    #/buytextbooks/detailtextbook.html/3(id or pk)/
    url(r'^detailtextbook.html/(?P<pk>[0-9]+)/$', views.TextbookDetailView.as_view(), name = 'detailtextbook'),

    #/buytextbooks/detailprepbook.html/3(id or pk)/
    url(r'^detailprepbook.html/(?P<pk>[0-9]+)/$', views.PrepbookDetailView.as_view(), name = 'detailprepbook'),

    #/buytextbooks/textbooks.html/
    url(r'^textbooks.html/', views.TextbookIndexView.as_view(), name='alltextbooks'),

    #/buytextbooks/prepbooks.html/
    url(r'^prepbooks.html/', views.PrepbookIndexView.as_view(), name='allprepbooks'),

    #/buytextbooks/sell.html/
    url(r'^sell.html/', views.sell, name='sell'),
    
    #/buytextbooks/blog.html/
    url(r'^blog.html/', views.blog, name='blog'),

    #/buytextbooks/signup.html/
    url(r'^signup.html/', views.signup, name='signup'),

    #/buytextbooks/login.html/
    url(r'^login.html/', views.login, name='login'),

    #/buytextbooks/textbook/add/
    url(r'^textbook/add/$', views.TextbookCreate.as_view(), name = 'textbook-add'),

    #/buytextbooks/prepbook/add/
    url(r'^prepbook/add/$', views.PrepbookCreate.as_view(), name = 'prepbook-add'),

    #/buytextbooks/textbook/3(id or pk)
    url(r'^textbook/(?P<pk>[0-9]+)/$', views.TextbookUpdate.as_view(), name = 'textbook-update'),

    #/buytextbooks/prepbook/3(id or pk)
    url(r'^prepbook/(?P<pk>[0-9]+)/$', views.PrepbookUpdate.as_view(), name = 'prepbook-update'),
    
]

