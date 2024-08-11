from django.db import models


# Create your models here.
class Uber(models.Model):
    uname=models.CharField(max_length=30)
    date=models.DateTimeField(auto_now=True,auto_now_add=False)
    location=models.CharField(max_length=1000)



    def __str__(self):
        return self.uname
