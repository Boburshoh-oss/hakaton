from rest_framework import generics
from rest_framework import views
from django.contrib.auth import get_user_model
from .serializers import UserRegisterSerializer, UserLoginSerializer
from rest_framework.response import Response
from django.shortcuts import redirect
from django.contrib.auth import login, logout
User = get_user_model()
# Create your views here.
class UserRegisterView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

class UserLoginView(views.APIView):
    def post(self,request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

class Logout(views.APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        logout(request)
        return redirect("login_view")
