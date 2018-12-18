from django.db import models
from django.utils import timezone
# Create your models here.
from company.models import Company
from tags.models import Tags
from subject.models import Subject
from django.contrib.auth.models import User
from profiles.models import Profile
from django.urls import reverse
from tinymce import HTMLField
from PIL import Image
from imagekit.models import ImageSpecField
from imagekit import ImageSpec, register
from imagekit.processors import ResizeToFill
"""
#This allows companies to group events into a fireside chat series or KPMG hackathon 2017, 2018. By looking at the attendees, StartCon etc.
#Companies should be able to add events across groups.
#For startcon, there are many talks in one conference. But then there's so many levels to it. E.g Startcon 2017 2018 has multiple talks etc.
class EventGroups(models.Model):
    title = models.CharField(max_length=100)
"""


class Event(models.Model):
    #blank = true allows for the form to submit with blank as an option.
    #if you want to change the author to profiles, import Profile and change User to Profile.
    #MAKE IT SO THAT IT DOESN'T SET NULL, JUST DOESNT SHOW.
    title = models.CharField(max_length=100)
    link = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(default='default.jpg', upload_to='event_images')
    image_thumbnail = ImageSpecField(source='image',
                                        processors=[ResizeToFill(100, 100)],
                                        format='JPEG',
                                        options={'quality': 60})
    start = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null= True)
    #ADD SOME EXCLUSIVITY! IF ONLY AVAILABLE FOR PEOPLE IN CERTAIN COUNTRIES OR CERTAIN UNIVERSITIES!!!
    #use javascript tinymce plugin for django for text editor for description
    #You are using crispyforms so its harder to override the html code.

    description = HTMLField('description')
    tags = models.ManyToManyField(Tags)
    subject = models.ManyToManyField(Subject)
    #this is currently a required function.
    attendees = models.ManyToManyField(User, related_name = 'attendees', blank=True)
    #eventgroup = models.ForeignKey(EventGroups, on_delete=models.SET_NULL, null=True), add a required=false in the form.


#add a tag system in so it can be searchable, events can be classified.
#add in the tags into the models.
    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('event:detail', kwargs={'pk': self.pk})

"""
    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
"""
