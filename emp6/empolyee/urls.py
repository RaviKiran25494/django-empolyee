from django.conf.urls import url
from.import views

urlpatterns = [
    url(r'^$', views.index ,name="index"),
    url(r'^(?P<register_id>[0-9]+)/$', views.detail,name='detail'),
    url(r'^next/(?P<id>\d+)$', views.next, name='next'),

    url(r'^reg1/$',views.registers,name='registers'),
    url(r'^registers1/$',views.registers1,name='registers1'),
    url(r'^registers1/create1$',views.create1,name='create1'),
    url(r'^registers1/join$',views.join,name='join'),
    url(r'^reg1/create$',views.create,name='create'),
    #login
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^signup/signup1$',views.signup1,name='signup1'),
    url(r'^login/$',views.login,name='login'),
]