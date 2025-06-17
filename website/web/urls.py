from django.urls import path
from . import views

urlpatterns = [
    path('',views.register,name='register'),
    path('viewst/',views.viewst,name='viewst'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('edit/<int:id>/', views.edit, name='edit')
]