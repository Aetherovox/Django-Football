from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager
# Create your models here.


class TokenizedUser(AbstractUser):
    username = models.CharField(max_length=40,unique=True,db_index=True)
    email = models.EmailField(max_length=254,unique=True)



class Profile(models.Model):
    user = models.OneToOneField(TokenizedUser, on_delete=models.CASCADE)
    image = models.ImageField(default= 'default.jpg', upload_to='profile_pics')
    def __str__(self):
        return f'{self.user.username} Profile'

