from django.db import models



class ShowModel(models.Model):
    First_name=models.CharField(max_length=20)
    Last_name=models.CharField(max_length=20)
    Email=models.EmailField(max_length=70,blank=True,unique=True)
    college_Name=models.CharField(max_length=50)
    gender=models.CharField(max_length=30)
    phone_No=models.IntegerField(blank=True,help_text='Contact phone number')
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    idea=models.TextField(default=True)
    problem=models.TextField(default=True)
    academic=models.CharField(max_length=30,default=True)
    link=models.CharField(max_length=30,default=True)
    team=models.CharField(max_length=20,default=True)
    hack_befor=models.CharField(max_length=20,default=True)
    hack_heard=models.CharField(max_length=30,default=True)