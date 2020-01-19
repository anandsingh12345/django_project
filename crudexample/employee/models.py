from django.db import models  
class Employee(models.Model):  
    eid = models.CharField(max_length=20,blank=False)  
    designation = models.CharField(max_length=50,blank=False) 
    dateofjoining = models.DateTimeField()
    name = models.CharField(max_length=50,blank=False) 
    address = models.TextField(max_length=200,blank=False)
    phonenumber = models.CharField(max_length=12,blank=False)
    email = models.EmailField(blank=False)  
    class Meta:  
        db_table = "employee"  
        unique_together = ["eid", "designation", "dateofjoining","name","address","phonenumber","email"]