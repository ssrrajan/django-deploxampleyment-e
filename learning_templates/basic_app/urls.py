from django.conf.urls import url,include
from basic_app import views


app_name = 'basic_app'

urlpatterns= [
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^others/$',views.others,name='others'),
]
