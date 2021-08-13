from django.urls import path, include
from. import views

urlpatterns =[
    path('', views.employee, name='EmployeePage'),
    path('add/', views.addemployee, name='EmployeeAddPage'),
    path('edit/', views.editemployee, name='EmployeeEditPage'),
    path('delete/', views.deleteemployee, name='EmployeeDeletePage'),
    path('search/', views.searchemployee, name='EmployeeSearchPage'),
]