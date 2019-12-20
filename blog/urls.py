from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('forms/', views.data_entry_form, name='form'),
    path('total_expanse', views.total_expanse, name='total_expanse'),

]
