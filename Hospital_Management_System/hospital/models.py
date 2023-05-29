from django.db import models



class Doctor(models.Model):
    Name = models.CharField(max_length= 25)
    Contact = models.IntegerField()
    Specialization = models.CharField(max_length=50)


class Patience(models.Model):
    Name = models.CharField(max_length=25)
    Gender = models.CharField(max_length=10)
    Contact = models.IntegerField(null=True)
    Address = models.TextField(max_length=50)



class Appointment(models.Model):
    Doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    Patience = models.ForeignKey(Patience,on_delete=models.CASCADE)
    Date = models.DateField()
    Time = models.TimeField()



    # Create your models here.