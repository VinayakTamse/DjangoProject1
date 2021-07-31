from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path("register/", views.Register, name="register"),
   path('login/', views.LoginHandle, name="login"),
   path('logout/', views.HandleLogout, name="logout"),
   path('contact/', views.Contact, name="contact"),
   path('members/', views.members, name="members"),
   path('delete/<int:mem_id>/',views.Delete_members, name="delete_members"),
   path('update/<int:id>/', views.update_members, name="update_members"),
]
