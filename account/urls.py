from django.urls import path
from .views import UserRegisterView, Logout,UserLoginView
from rest_framework.authtoken.views import obtain_auth_token 

urlpatterns = [
    path('register/',UserRegisterView.as_view()),
    path('login/',UserLoginView.as_view(),name="login_view"),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('logout/',Logout.as_view()),
    ]