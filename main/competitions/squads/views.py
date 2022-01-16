from django.shortcuts import get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from .models import Squad
from .players.models import Player
# Create your views here.


class SquadListView(ListView):
    model = Squad
    context_object_name = 'squads'

class SquadDetailView(DetailView):
    model = Squad

class SquadCreateView(LoginRequiredMixin,CreateView):
    model = Squad

    @staticmethod
    def get_success_url():
        return reverse('squad-list')


    def form_valid(self,form):
        if form.instance.author == self.request.user:
            return super().form_valid(form)




class SquadUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Squad

    @staticmethod
    def get_success_url():
        return reverse('squad-detail')

    def form_valid(self,form):
        if form.instance.author == self.request.user:
            return super().form_valid(form)

    def test_func(self):
        squad = self.get_object()
        if self.request.user == squad.user:
            return True
        return False


class SquadDeleteView(LoginRequiredMixin,DeleteView):
    model = Squad

    @staticmethod
    def get_success_url():
        return reverse('squad-list')

    def test_func(self):
        squad = self.get_object()
        if self.request.user == squad.user:
            return True
        return False


class SquadRosterView(ListView):
    model = Player
    context_object_name = 'roster'

    def get_query_set(self):
        element = get_object_or_404(Squad,id=self.kwargs.get('id'))
        return Player.objects.filter(squads__id=element)