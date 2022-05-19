from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import include
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    re_path(r'^$', index, name="index"),
    re_path(r'^dept/(?P<dept>[a-z]+)/$', dept, name="dept"),
    re_path(r'^payment/(?P<dept>[a-z]+)/(?P<pk>[0-9]+)/$', payment, name="instruction"),
    # re_path(r'^pay/$', payments, name="instruction"),
    re_path(r'^backup/(?P<bk_key>[a-z]+)/$', backup, name="backup"),
    re_path(r'^payment/upload/$', addNewReport, name="pay_report"),
    re_path(r'^(?P<type_report>[a-z]+)/report/$', report, name="report"),
    re_path(r'dashboard/payment/$', DashboardPaymentSerializerList.as_view()), 
    re_path(r'dashboard/user/$', DashboardUserSerializerList.as_view()), 
    re_path(r'robot/count/$', RobotUserSerializerList.as_view()), 
    re_path(r'payment/csv/(?P<dept>[-\w]+)/$', PaymentSerializerList.as_view()), 
    re_path(r'user/(?P<val>[a-z]+)/$', userfn,name='data_user'), 
    re_path(r'depts/', department,name='departments'), 
    re_path(r'workshop/', workshop,name='workshop'),
    re_path(r'project/', project.as_view(extra_context = {'title': 'Project Detials'}),name='project'),


    # re_path(r'char/charts/$', userfn,name='data_user'), 
    # re_path(r'^register/$', register, name="register"),
    # re_path(r'^uitest/$', test, name="test"),
    # re_path(r'^login/',user_login, name='login'),
    # re_path(r'^logout/',user_logout, name='logout'),
    # re_path(r'^add/',addAnnouncement, name='add'),
    # re_path(r'^delete/(?P<pk>[0-9]+)/$',delAnnouncement, name='delete'),
    # re_path(r'^edit/(?P<pk>[0-9]+)/$',editAnnouncement, name='edit'),
    # re_path(r'^track/$',outbreak, name='track'),

    # re_path(r'^logout/$', auth_views.logout, {'template_name': 'announcements/logged_out.html'}, name='logout'),

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
