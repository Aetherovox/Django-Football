from django.contrib import admin
from .models import Profile,TokenizedUser
# Register your models here.

class TokenizedUserAdmin(admin.ModelAdmin):
    model = TokenizedUser


admin.site.register(Profile)
admin.site.register(TokenizedUser)