from django.urls import path
from .views import *

urlpatterns=[
    path('login/',user_login,name="login"),
    path('sign-up/',sign_up,name="sign_up"),
    path('logout/',user_logout)
]