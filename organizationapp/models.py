from django.db import models
from django.contrib.auth.models import User
from django.core.validators import ValidationError
# Create your models here.


def validate_location_count(count):
        if not count.isdigit():    
            raise ValidationError('%(phone)s must be digits ')
        
class OrganizationDetails(models.Model):
    email = models.ForeignKey(to=User,on_delete=models.CASCADE)
    org_name = models.CharField(max_length=500)
    org_type = models.CharField(max_length=500) 
    phone_number = models.CharField(max_length=500)
    license_number = models.CharField(max_length=500)
    location_count = models.CharField(verbose_name="Location Count", max_length=1,  
    validators=[validate_location_count], default='1')

    
class locationDetails(models.Model):    
    email = models.ForeignKey(to=User,on_delete=models.CASCADE)
    location_name = models.CharField(max_length=500)
    location_address = models.CharField(max_length=500)
    # location_status = models.BooleanField()

class billingDetails(models.Model):
    email = models.ForeignKey(to=User,on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=500)
    plan_status = models.BooleanField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

class YearlyPlans(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.CharField(max_length=10)
    type_plan = models.CharField(max_length=100)
    locations_count = models.CharField(verbose_name="Location count of plan ",max_length=10)
    description = models.CharField(verbose_name = "Plan Description",max_length=500,default="Includes all features! Unlimited Visitors")

    class Meta:
        verbose_name = "Yearly Plans"
    
    def get_monthly_price(self):
        return int(int(self.price)/12)
