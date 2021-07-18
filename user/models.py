from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    photo = CloudinaryField('profile_pics/', blank=True, default = 'image')

    def __str__(self):
        return self.user.username
    
    def save_profile(self):
        self.save()                   

    def delete_profile(self):
        self.delete()
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles' 