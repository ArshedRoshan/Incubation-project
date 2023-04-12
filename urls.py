from django.contrib import admin
from.import views
from django.urls import path
from .views import *


urlpatterns = [
    path('adminlog',adminlog.as_view(),name='adminlog'),
    path('users',users.as_view(),name='users'),
    path('userdel/<int:id>',delete.as_view(),name='userdel'),
    path('update/<int:id>',Update.as_view(),name='update'),
    path('company_list',company_list.as_view(),name='company_list'),
    path('company_detail/<int:id>',company_detail.as_view(),name='company_detail'),
    path('pend_list/<int:id>',pend_list.as_view(),name='pend_list'),
    path('pend_list1',pend_list1.as_view(),name='pend_list1'),
    path('accept/<int:id>',accept.as_view(),name='accept'),
    path('accept',accept1.as_view(),name='accept1'),
    path('decline/<int:id>',Decline.as_view(),name='decline'),
    path('application',application.as_view(),name='application'),
    path('get_approved',get_approved.as_view(),name='get_approved'),
    path('booking',booking.as_view(),name='booking'),
    path('get_all', get_all.as_view(),name='get_all')
    
]
