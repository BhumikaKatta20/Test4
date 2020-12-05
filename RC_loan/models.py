from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import post_save

# Create your models here.
class Agent_block(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	Date_of_birth=models.DateField("Date",default=datetime.now)
	Location=models.CharField(max_length=50,default='')
	Address=models.CharField(max_length=150,default='')
	city=models.CharField(max_length=50,default='')
	Phone_number=models.IntegerField(default=0)
def create_profile(sender,**kwargs):
	if kwargs['created']:
		Agentblock=Agent_block.objects.create(user=kwargs['instance'])
post_save.connect(create_profile, sender=User)

class customer_block(models.Model):
	Customer_name=models.CharField(max_length=50,default='')
	Location=models.CharField(max_length=50,default='')
	Address=models.CharField(max_length=50,default='')
	stipend=models.IntegerField(default=0)
	city=models.CharField(max_length=50,default='')
	
class loan_data(models.Model):
	user_name=models.CharField(max_length=50,default='')
	first_name=models.CharField(max_length=50,default='')
	last_name=models.CharField(max_length=50,default='')
	email=models.CharField(max_length=50,default='')
	adhaar_card=models.CharField(max_length=50,default='')
	pan_card=models.CharField(max_length=50,default='')
	phone_number=models.CharField(max_length=50,default='')
	#Date_of_birth=models.DateField("Date",default=datetime.now)
	Date_of_apply=models.DateField("Date",default=datetime.now)
	Approve=models.CharField(max_length=50,default='')
	Agent_name=models.CharField(max_length=50,default='')
	loan_amount=models.CharField(max_length=50,default='')
	monthly=models.CharField(max_length=50,default='')
	year=models.CharField(max_length=50,default='')
	total_interest=models.CharField(max_length=50,default='')
	Address=models.CharField(max_length=50,default='')
