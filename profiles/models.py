from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit import ImageSpec, register
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField
# Create your models here.

#insert university, continent etc. Some global events such as coding events don't
#should this be submitted by users or companies? Preferably companies.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    linkedin = models.URLField(max_length=200, default='')
    position = models.CharField(max_length=100, default='')

    #saved = models.ManyToManyField(Event, related_name = 'saved', blank=True)


    #this renames it in the database so it's not just Profile.object(1)
    def __str__(self):
        return f'{self.user.username} Profile'
"""
    initially has to be user generated? 
    university =
    image = ProcessedImageField(default='default_profile.jpg', upload_to='profile_pics',
                                processors=[ResizeToFill(300,300)],
                                format = 'JPEG',
                                options={'quality': 60})

"""
