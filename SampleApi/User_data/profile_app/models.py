from django.db import models

# Create your models here.
class Detail(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    mobile = models.IntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    Image = models.ImageField(default="",)
    
