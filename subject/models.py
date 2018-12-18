from django.db import models

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

#SHOULD HAVE A USER FOLLOWING MANY SUBJECTS THEY ARE INTERESTED IN.
