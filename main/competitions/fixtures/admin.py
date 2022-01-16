from django.contrib import admin
from .models import Fixture,Prediction,Team, TeamScore
# Register your models here.

admin.site.register(Fixture)
admin.site.register(Prediction)
admin.site.register(Team)
admin.site.register(TeamScore)
