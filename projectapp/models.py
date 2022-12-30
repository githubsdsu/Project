from django.db import models

# Create your models here.
class Signup(models.Model):
    firstname=models.TextField(default=None)
    lastname=models.TextField(default=None)
    username=models.TextField(default=None)
    password=models.TextField(default=None)
    confirmpassword=models.TextField(null=True,blank=True,default="0")
    mailbox=models.TextField(null=True,blank=True,default="0")
class Forgot(models.Model):
     username=models.TextField(default=None)
     mailbox=models.TextField(default=None)
class OTP(models.Model):
     otp=models.IntegerField(default=None)
class Update(models.Model):
     username=models.TextField(default=None)
     password=models.TextField(default=None)
     confirmpassword=models.TextField(default=None)
class Login(models.Model):
     username=models.TextField(default=None)
     password=models.TextField(default=None)
class Facescan(models.Model):
   
     
     username = models.CharField(max_length=50,default="")
     image = models.ImageField(upload_to='uploads/',default=False)
def __str__(self):
     
     return self.title
class Result(models.Model):
     username=models.TextField(default=None)
class History(models.Model):
     mailbox=models.TextField(null=True,blank=True,default="0")  
     username=models.TextField(null=True,blank=True,default="0")