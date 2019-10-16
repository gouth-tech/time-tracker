from django.urls import path
from api.views import UserRegistrationAPIView, UserLoginAPIView

app_name = 'api'

urlpatterns = [
    path('users/sign-up/', UserRegistrationAPIView.as_view(), name="list"),
    path('users/login/', UserLoginAPIView.as_view(), name="login"),

]
