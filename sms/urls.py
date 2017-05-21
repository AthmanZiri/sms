from django.conf.urls import url

from sms import views

urlpatterns = [
	
	url(r'^list/', views.sms_list, name='sms_list'),

    url(r'^', views.sms_create, name='sms_create'),
    
]
