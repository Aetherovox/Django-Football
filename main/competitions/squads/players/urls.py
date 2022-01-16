from django.urls import path
from .views import (PlayerListView, PlayerDetailView, PlayerHistoryDetailView, PlayerHistoryListView)
urlpatterns = [
    path('', PlayerListView.as_view(), name='player-list'),
    path('player/<int:pk>', PlayerDetailView.as_view(), name='player-detail'),
    # TODO: use Javascript to render player history within the detail view
    path('player/<int:player>/history/', PlayerHistoryListView.as_view(), name='playerhistory_list'),
    #path('player/history/', PlayerHistoryListView.as_view(), name='playerhistory_list'),
    # path('player/<int:player>/history/<int:pk>', PlayerHistoryDetailView.as_view(), name='playerhistory_detail'),
    path('player/history/<int:pk>', PlayerHistoryDetailView.as_view(), name='playerhistory_detail'),

]
