from django.urls import path
from .views import SquadListView, SquadDetailView, SquadCreateView, SquadUpdateView, SquadDeleteView
urlpatterns = [
    path('Squad/', SquadListView.as_view(), name='squad-list'),
    path('Squad/<int:pk>', SquadDetailView.as_view(), name='squad-detail'),
    path('Squad/new', SquadCreateView.as_view(), name='squad-create'),
    path('Squad/<int:pk>', SquadUpdateView.as_view(), name='squad-update'),
    path('Squad/<int:pk>', SquadDeleteView.as_view(), name='squad-delete')
]
