from django.db import models
from Chairman.models import *
from django.utils import timezone
import math



# Create your models here.
class House(models.Model):
    house_no=models.IntegerField(unique=True,null=True,blank=True)
    status=models.CharField(max_length=10, default=" ")
    details=models.CharField(max_length=100,default=" ")


    def __str__(self):
        return str(self.house_no)

class Member(models.Model):
    #user_id = models.ForeignKey(User,on_delete=CASCADE)
    user_id = models.ForeignKey(User,on_delete=CASCADE, related_name='Member',null=True) 
    #house_no=models.IntegerField(unique=True,null=True,blank=True)
    house_no = models.ForeignKey(House,on_delete=CASCADE,related_name='House',null=True)
    firstname = models.CharField(max_length=50)
    lastname =models.CharField(max_length=50)
    gender=models.CharField(max_length=20)
    contact = models.CharField(max_length=11)
    occupation=models.CharField(max_length=50)
    job_address=models.TextField(max_length=500)
    birthdate=models.DateField(max_length=20,blank=True,null=True)  
    marital_status=models.CharField(max_length=20)
    no_of_members=models.CharField(max_length=20)
    native=models.CharField(max_length=100)
    nationality=models.CharField(max_length=100, default="Indian")
    no_of_vehicles=models.CharField(max_length=100)
    vehicle_type=models.CharField(max_length=100)
    id_proof=models.FileField(upload_to='media/images',default='media/default.png')
    profile_pic=models.FileField(upload_to='media/images',default='media/default.png')
    #id_proof=models.AutoField(primary_key=True)


    
    def __str__(self):
        return self.firstname +" "+ str(self.house_no.house_no)

class Notice(models.Model):
    
    title = models.CharField(max_length=50)
    description =models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True) 
    pic=models.FileField(upload_to='media/images/',null=True,blank=False)
    video=models.FileField(upload_to="media/videos/",null=True, blank=False)


    def __str__(self):
        return str(self.title)
    
    def whenpublished(self):
        now = timezone.now()
        
        diff= now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            if seconds == 1:
                return str(seconds) +  "second ago"
            
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"
            
            else:
                return str(minutes) + " minutes ago"



        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            

            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"


        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"

    def noticeViewCount(self):
            ncount=NoticeView.objects.filter(notice_id=self.id).count()

            if ncount>1:
                return str(ncount)+ "views"
            else:
                return str(ncount)+ "view"




class NoticeView(models.Model):
    notice_id=models.ForeignKey(Notice,on_delete=models.CASCADE)
    member_id=models.ForeignKey(Member,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return self.member_id.firstname+ " "+ self.notice_id.title  

class Complain(models.Model):
    
    title = models.CharField(max_length=50)
    description =models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True) 
    pic=models.FileField(upload_to='media/images/',null=True,blank=True)
    #video=models.FileField(upload_to="media/videos/",null=True, blank=False)


    def __str__(self):
        return str(self.title)


class ComplainView(models.Model):
    complain_id=models.ForeignKey(Complain,on_delete=models.CASCADE)
    member_id=models.ForeignKey(Member,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return self.member_id.firstname+ " "+ self.complain_id.title 

class Event(models.Model):
    
    title = models.CharField(max_length=50)
    description =models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True) 
    pic=models.FileField(upload_to='media/images/',null=True,blank=False)
    video=models.FileField(upload_to="media/videos/",null=True, blank=False)


    def __str__(self):
        return str(self.title)
    
    def whenpublished(self):
        now = timezone.now()
        
        diff= now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            if seconds == 1:
                return str(seconds) +  "second ago"
            
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"
            
            else:
                return str(minutes) + " minutes ago"



        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            

            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"


        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"

    def eventViewCount(self):
            ecount=EventView.objects.filter(event_id=self.id).count()

            if ecount>1:
                return str(ecount)+ "views"
            else:
                return str(ecount)+ "view"




class EventView(models.Model):
    event_id=models.ForeignKey(Event,on_delete=models.CASCADE)
    member_id=models.ForeignKey(Member,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return self.member_id.firstname+ " "+ self.event_id.title  
