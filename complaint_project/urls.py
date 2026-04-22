
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('delete/<int:id>/', views.delete_complaint),
    path('edit/<int:id>/', views.edit_complaint),
]
