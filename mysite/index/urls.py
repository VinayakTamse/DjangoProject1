from django.contrib import admin
from django.urls import path
from .views import Index, gallery, Register, Login_View, LogoutMethod

urlpatterns = [

    path("", Index.as_view(), name="indexpage"),
    path('gallery/', gallery, name='gallery'),
    path('register/', Register.as_view(), name='register'),
    path('login/', Login_View.as_view(), name='login'),
    path('logout/', LogoutMethod.as_view(), name='logout'),




]