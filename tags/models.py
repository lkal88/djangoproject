from django.db import models

# Create your models here.
#SHOULD WE HAVE A SEPARATE DATABASE THAT CONTAINS THE TAGS/SUBJECTS FOR THE EVENTS?
#need to create one for cities as well maybe? atm only sydney so should be ok.
class Tags(models.Model):
    #the tags should have a many-to-many function with the events.
    #should be able to add tags and subtract tags.
    #should be able to choose from a list of tags.
    #should it be split into core categories: type/core of event (Networking, talk, scholarship, competition, webinar, Professional Development, opportunity)
    #and core/tags (entrepreneurship, engineering, startups etc, management consulting, finance etc.)
    #maybe make this CHOICES! rather than separate MODELS!. Can think about it later.
    #networking engineering events, entrepreneurship talks etc.
    #UNSW HAS REGISTRATIONAL ESSENTIAL.
    name = models.CharField(max_length=100)
    #make sure u make it self.name
    def __str__(self):
        return f'{self.name}'


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'





#class Type(models.Model):
