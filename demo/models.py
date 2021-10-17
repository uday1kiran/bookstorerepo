from django.db import models

# Create your models here.
from django.db import models
class Book(models.Model):
    STATUSES={
   ("Un",'Unknown'),
 ("pr",'processed'),
 ("paid",'paid')
    }
    title=models.CharField(max_length=36)
    image = models.ImageField(upload_to='images/',blank=True)
    status=models.CharField(max_length=36,choices=STATUSES)

    def __str__(self):  # string representation of an object.this method used for.
        return self.title
