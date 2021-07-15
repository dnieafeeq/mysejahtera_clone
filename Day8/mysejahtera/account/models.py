from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.jpeg', upload_to = 'profile_pics')
    full_name = models.CharField(default='pls update', max_length=250)
    nric = models.CharField(default='pls update', max_length=15)
    phone_no = models.CharField(default='pls update', max_length=25)
    state = models.CharField(default='pls update', max_length=50)

    def __str__(self):
        return f'{self.user.username}'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)