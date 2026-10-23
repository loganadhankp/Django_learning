from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='student_home'),
    path('products/', views.products_list, name='products_list'),
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),
    path('base/', views.base, name='base'),

]