from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name="index"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.register, name="signup"),
    path('logout/', views.logoutPage, name="logout")

]

