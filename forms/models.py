from django.db import models
from django.contrib.auth.models import User
# Create your models here

class Form(models.Model):
    Student_Name=models.CharField(max_length = 100)
    College_Name= models.CharField(max_length = 100)
    Specialization = models.CharField(max_length = 100,default="",blank=False)
    Degree_Name =models.CharField(max_length = 100,default="",blank=False)
    Intern =models.CharField(max_length = 100,default="",blank=False)
    Phone_No =models.CharField(max_length = 100,default="",blank=False)
    Email_id =models.CharField(max_length = 100,default="",blank=False)
    City =models.CharField(max_length = 100,default="",blank=False)
    Gender =models.CharField(max_length = 100,default="",blank=False)    
    notes= models.TextField(blank=True)
    user= models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.Student_Name