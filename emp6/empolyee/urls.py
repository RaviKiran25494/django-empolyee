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
    # url(r'^signup/$',views.signup,name='signup'),
    # url(r'^signup/signup1$',views.signup1,name='signup1'),
    url(r'^login/$',views.login,name='login'),
    url(r'^login/loginnet$',views.loginnet,name='loginnet'),
    #leavestatus
    url(r'^leave/$',views.leave,name='leave'),
    url(r'^leave/leave1$',views.leave1,name='leave1'),
    url(r'^apprioved1/(?P<id>\d+)$',views.apprioved1,name='apprioved1'),
    url(r'^login123/$',views.login123,name='login123'),
    url(r'^leavestatus/$',views.leavestatus,name='leavestatus'),
    url(r'^empdetails1/$',views.empdetails1,name='empdetails1'),
    url(r'^payslips/$',views.payslips,name='payslips'),

    #loginadmin
    url(r'^signupa/$',views.signupa,name='signupa'),
    url(r'^signupa/signupa1$',views.signupa1,name='signupa1'),
    url(r'^logina/$',views.logina,name='logina'),
    url(r'^logina/logina1$',views.logina1,name='logina1'),
    url(r'^empdetails/$',views.empdetails,name='empdetails'),
    url(r'^payments/$',views.payments,name='payments'),
    url(r'^payments/payment1$',views.payments1,name='payments1'),
    url(r'^leaveapprioved/$',views.leaveapprioved,name='leaveapprioved'),
    url(r'^forgot/$',views.forgot,name='forgot'),
    url(r'^forgot/forgot1$',views.forgot1,name='forgot1'),
    url(r'^login123/$',views.login123,name='login123'),


    
    url(r'^home/$',views.home,name='home'),
    url(r'^logout/$',views.logout,name='logout'),

    url(r'^signup/$',views.UserFormView.as_view(),name='signup'),
]