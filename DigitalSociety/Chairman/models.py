
from statistics import mode
from django.db import models
from django.db.models.deletion import CASCADE



# Create your models here.

class User(models.Model):
      email = models.EmailField(unique=True)
      password = models.CharField(max_length=20)
      otp =models.IntegerField(default=459)
      is_active = models.BooleanField(default=True)
      is_verified = models.BooleanField(default=False)
      role = models.CharField(max_length=10)
      first_time_login=models.BooleanField(default=False)
      created_at = models.DateTimeField(auto_now_add=True,blank=False)
      updated_at = models.DateTimeField(auto_now=True,blank=False)

      def __str__(self):
          return self.email+ "- "+self.role

class Chairman(models.Model):
      user_id = models.ForeignKey(User,on_delete=CASCADE)
      firstname = models.CharField(max_length=50)
      lastname =models.CharField(max_length=50)
      contact = models.CharField(max_length=11)
      address=models.TextField(max_length=500)
      profile_pic=models.FileField(upload_to='media/images',default='media/default.png')
      gender = models.CharField(max_length=30)

      def __str__(self):
          return self.firstname




