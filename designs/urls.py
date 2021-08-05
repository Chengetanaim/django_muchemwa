from django.urls import path
from . import views
app_name = 'designs'
urlpatterns = [
    path('', views.index, name='index'),
    path('tshirts/', views.tshirts, name='tshirts'),
    path('jeans/', views.jeans, name='jeans'),
    path('shoes/', views.shoes, name='shoes')
]
