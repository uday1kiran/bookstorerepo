from django.db import models

# Create your models here.
from django.db import models
class Book(models.Model):
    STATUSES={
   (0,'Unknown'),
 (1,'processed'),
 (2,'paid')
    }
    title=models.CharField(max_length=36,choices=STATUSES)
    image = models.ImageField(upload_to='images/')

    def __str__(self):  # string representation of an object.this method used for.
        return self.title
