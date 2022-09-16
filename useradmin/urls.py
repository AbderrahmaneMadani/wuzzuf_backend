from django.urls import path
from . import views


urlpatterns = [
    #path('', views.index, name='index'),
    #path('', views.index1, name='index1'),
    path('useradmin' , views.useradmin , name = 'useradmin'),
    path('', views.useradmins, name = 'useradmins'),
]