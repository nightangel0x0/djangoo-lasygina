from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('chat', views.chat,name='chat'),
    path('firstroom',views.first,name='first'),
    path('secondroom', views.second,name='second'),
    path('thirdroom', views.third, name='third')
]
