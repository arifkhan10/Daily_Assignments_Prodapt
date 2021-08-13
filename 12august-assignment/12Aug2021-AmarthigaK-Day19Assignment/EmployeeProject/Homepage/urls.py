from django.urls import path, include
from. import views

urlpatterns = [
    path('', views.Homepage, name="Welcome to my home page"),
    path('contact/', views.contactpage, name="Welcome to my contact page"),
    path('gallery/', views.gallerypage, name="Welcome to my gallery page"),
]