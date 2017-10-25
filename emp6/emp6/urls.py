from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^empolyee/', include("empolyee.urls")),
    url(r'^logout/', auth_views.logout, {'next_page': '/empolyee'}, name='logout'),

    
]
