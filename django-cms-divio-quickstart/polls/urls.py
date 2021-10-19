from django.urls import path,url
from . import views
urlpatterns = [
    url(r'^data/(?P<id>\d+/$', views.test,),
    path('', views.index, name='index'),
    path('index1/<int:id>/', views.templatefn , name='index')
]