from django.urls import path,include
from .views import Competitions,ParticipantsView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'',Competitions,'competitions')
router.register(r'participants',ParticipantsView,'participants')


urlpatterns = [
    path('',include(router.urls)),

]



