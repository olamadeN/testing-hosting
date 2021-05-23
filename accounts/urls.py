from django.urls import path
from . import views

app_name="accounts"

urlpatterns = [
    path('', views.landpage, name="landpage"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.LogIn, name="login"),
     path('useraccount/', views.useraccount, name="useraccount"),
]