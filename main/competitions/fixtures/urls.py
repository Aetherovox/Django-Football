from django.urls import path,include
from .views import FixtureAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# TODO: FixturesAPIView must have a competition ID slug
router.register(r'(?P<comp>.+)',FixtureAPIView,'fixtures')
# router.register(r'',TeamAPIView,'teams')

urlpatterns = [
    path('',include(router.urls)),

]

