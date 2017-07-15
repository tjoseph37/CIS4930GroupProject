from django.conf.urls import url
from . import views 

urlpatterns= [

url(r'^$',views.index,name='index' ),
url(r'^contact/$', views.contact, name='contact'),
url(r'^about', views.about, name='about'),
url(r'^flowers', views.flowers, name='flowers'),
url(r'^encrypt', views.encrypt, name='encrypt'),
url(r'^page2', views.page2, name='page2'),
url(r'^bluetooth', views.bluetooth, name='bluetooth'),
url(r'^page3', views.page3, name='page3'), 
url(r'^page4', views.page4, name='page4'),
url(r'^page5', views.page5, name='page5'),
url(r'^success', views.success, name='success'),
]
