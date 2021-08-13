from django.urls import path, include
from. import views

urlpatterns =[
    path('', views.company, name='CompanyPage'),
    path('add/', views.addcompany, name='CompanyAddPage'),
    path('edit/', views.editcompany, name='CompanyEditPage'),
    path('delete/', views.deletecompany, name='CompanyDeletePage'),
    path('search/', views.searchcompany, name='CompanySearchPage'),
]