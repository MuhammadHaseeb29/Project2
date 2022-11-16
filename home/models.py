from django.db import models

class Employee(models.Model):
     eid = models.CharField(max_length=20)
     ename = models.CharField(max_length=100)
     eemail = models.EmailField()
     econtact = models.CharField(max_length=20)

class UserDataForm(models.Model):
     eid = models.CharField(max_length=20)
     eemail = models.EmailField()
     epassword1 = models.CharField(max_length=100)
     epassword2 = models.CharField(max_length=20)
