from django.db import models
from django.contrib import admin
class Customer(models.Model):
        Name=models.CharField(max_length=10)
        Accno=models.IntegerField(primary_key="Accno")
        DoB=models.DateField()
        Address=models.CharField(max_length=25)
        Email=models.EmailField()

class CustomerAdmin(admin.ModelAdmin):
        list_display=('Name','Accno','DoB','Address','Email')
