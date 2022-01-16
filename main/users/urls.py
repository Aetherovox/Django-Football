from django.urls import path
from .views import UserCreationView,CustomObtainTokenPair,current_user

urlpatterns = [
    path('create/', UserCreationView.as_view(), name='create_user'),
    path('current_user/',current_user,name='current_user'),
    path('custom_auth/',CustomObtainTokenPair.as_view(),name='custom_token_pair')
]
