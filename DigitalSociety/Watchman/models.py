from django.db import models
from Chairman.models import *

# Create your models here.

class Watchman(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    ID_pic=models.FileField(upload_to="media/documents",default="media/default.png")
    profile_pic=models.FileField(upload_to="media/images",default="media/default.png")

    def __str__(self):
        return self.firstname