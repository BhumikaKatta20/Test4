from django.shortcuts import render, redirect
from RC_loan.forms import Agent_block,RegistrationForm
import re
import sys
from django.db.models import Q
import pandas as pd
import sqlite3
from datetime import date
#import auth_user
from django.contrib.auth.models import User

from RC_loan.models import loan_data
def login_redirect(request):
	return redirect('index')

def index(request):
	title="RC"
	return render(request,'index.html',{'title':title})

#--------------------Registration of Agent and Customer------------------------

def Agent_register(request):
	title="Register"
	if request.method == 'POST':
		form =Agent_block(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login_redirect')
	else:
		form = Agent_block()
	backgrd = 'wal.jpg'
	return render(request,'Form_base/register_cust.html',{'form':form,'title':title})

# Registration of Client
def user_create(request):
	title="Register"
	if request.method =='POST':
		form=RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form=RegistrationForm()
	return render(request,'Form_base/user_create.html',{'form':form,'title':title})

#-----------------------------List view and update the user---------------------------------

def customer_list(request):
	title='Customer List'
	Cdata =User.objects.filter(is_staff=0)
	
	return render(request,'view_data/customer_list.html',{'title':title,'Cdata':Cdata})

def cust_edit(request,id):
	print(id)
	Cdata=User.objects.get(id=id)

	return render(request,'Form_base/cust_edit.html',{'Cdata':Cdata})
def cust_update(request):
	print('upadte')
	flag=False
	ida=request.GET['id_val']
	user_name=request.GET['user_name']
	first_name=request.GET['first_name']
	first_name_error=' '
	a = re.findall(r'[0-9@!$%#*^]', first_name)
	if len(a) > 0:
		flag = True
		first_name_error = 'numbers, @, #, *, !, %, $, ^ are not vaild'
	last_name=request.GET['last_name']
	last_name_error=' '
	a = re.findall(r'[0-9@!$%#*^]', last_name)
	if len(a) > 0:
		flag = True
		last_name_error = 'numbers, @, #, *, !, %, $, ^ are not vaild'
	email=request.GET['email']
	Cdata =User.objects.filter(is_staff=0)
	
	if flag==True:
		print('a')
		return render(request,'Form_base/cust_edit_re.html',{'Cdata':Cdata,
			'id':ida,'first_name':first_name,'last_name':last_name,'email':email,'user_name':user_name
			,'first_name_error':first_name_error,'last_name_error':last_name_error})
	else:
		A = User.objects.filter(id=ida).update(first_name=first_name, last_name=last_name, email=email)
		return render(request,'view_data/customer_list.html',{'Cdata':Cdata})

def cust_edit_re(request):
	print('upadte')
	flag=False
	ida=request.GET['id_val']
	user_name=request.GET['user_name']
	first_name=request.GET['first_name']
	first_name_error=' '
	a = re.findall(r'[0-9@!$%#*^]', first_name)
	if len(a) > 0:
		flag = True
		first_name_error = 'numbers, @, #, *, !, %, $, ^ are not vaild'
	last_name=request.GET['last_name']
	last_name_error=' '
	a = re.findall(r'[0-9@!$%#*^]', last_name)
	if len(a) > 0:
		flag = True
		last_name_error = 'numbers, @, #, *, !, %, $, ^ are not vaild'
	email=request.GET['email']
	Cdata =User.objects.filter(is_staff=0)
	
	if flag==True:
		print('a')
		return render(request,'Form_base/cust_edit_re.html',{'Cdata':Cdata,
			'id':ida,'first_name':first_name,'last_name':last_name,'email':email,'user_name':user_name
			,'first_name_error':first_name_error,'last_name_error':last_name_error})
	else:
		A = User.objects.filter(id=ida).update(first_name=first_name, last_name=last_name, email=email)
		return render(request,'view_data/customer_list.html',{'Cdata':Cdata})


#--------------------------------Apply for Loan--------------------------------

def apply_for_loan(request):
	title="apply_for_loan"
	return render(request,'Form_base/apply_for_loan.html',{'title':title})


#application text condition
def smit(request):
	flag = False
	title='loan applition'
	total_intrest=request.GET['total_intrest']
	total_amount=request.GET['total_amount']
	monthly=request.GET['monthly']
	user_name=request.GET['user_name']
	user_name_error=' '
	if User.objects.filter(username=user_name).exists():
		print(user_name)
	else:
		user_name_error='user does not Does Not Exist'
	
	first_name=request.GET['first_name']
	first_name_error=' '
	a = re.findall(r'[0-9@!$%#*^]', first_name)
	if len(a) > 0:
		flag = True
		first_name_error = 'numbers, @, #, *, !, %, $, ^ are not vaild'
	last_name=request.GET['last_name']
	last_name_error=' '
	a = re.findall(r'[0-9@!$%#*^]', last_name)
	if len(a) > 0:
		flag = True
		last_name_error = 'numbers, @, #, *, !, %, $, ^ are not vaild'
	email=request.GET['email']
	Address = request.GET['Address']
	Address_error = ' '
	a = re.findall(r'[@!$%]', Address)
	print(a)
	if len(a) > 0:
		flag = True
		Address_error = '@ , !, %, $, ^ are not vaild'
	adhaar_card=request.GET['adhaar_card']
	adhaar_card_error=' '
	p = request.GET['adhaar_card']
	if  len(p) != 12:
		flag = True
		adhaar_card_error = 'only 12 digits are valid'
	
	pan_card=request.GET['pan_card']
	pan_card_error=' '
	if  len(pan_card) != 10:
			flag = True
			pan_card_error = 'Invalid'
	phone_number=request.GET['phone_number']
	phone_number_error=' '
	amount=request.GET['loan_amount']
	loan_amount_error=' '
	if int(amount)>5000000:
		flag=True
		loan_amount_error='Amount should be less than 50,00,000'
	year=request.GET['year']
	year_error=' '
	if int(year)>10:
		flag=True
		year_error='Time should be less than 10 years'
	p = request.GET['phone_number']
	if  len(p) != 10:
		flag = True
		phone_number_error = 'only 10 digits are valid'
	
	if flag==True:
		
		return render(request,'Form_base/apply_for_loan_error.html',{'loan_amount':amount,'year':year,'year_error':year_error,
		'title':title,'first_name':first_name,'user_name':user_name,'email':email,'loan_amount_error':loan_amount_error,
		'phone_number':phone_number,'pan_card':pan_card,'adhaar_card':adhaar_card,'Address':Address,'last_name':last_name,
		'phone_number_error':phone_number_error,'pan_card_error':pan_card_error,'adhaar_card_error':adhaar_card_error,
		'Address_error':Address_error,'last_name_error':last_name_error,'first_name_error':first_name_error,
		'user_name_error':user_name_error})
	else:
		name=str(request.user)
		id_val = sys.getsizeof(loan_data) 
		
		print(id_val)
		if id_val<0:
			id_val=0
		else:
			id_val=id_val+1

		a = loan_data(
	user_name=user_name,first_name=first_name,last_name=last_name,email=email,adhaar_card=adhaar_card,
	pan_card=pan_card,phone_number=phone_number,Date_of_apply=str(date.today()),Approve='New',
	Agent_name=name,loan_amount=amount,monthly=monthly,year=year,total_interest=total_intrest,Address=Address)
		
		a.save()
		Cdata =loan_data.objects.filter(Approve='New')
		print(loan_data
			)
		print('##################################')
		#print(datt)
		return redirect('index')



#-------------------------------View the Loan Applications-----------------------------------

# (application view for Agent) and (super user to view approve table)Agent_name=request.user
def Applications(request):
	title='Applications'
	if request.user.is_authenticated:
		Cdata =loan_data.objects.filter(user_name=request.user)
	
	if request.user.is_staff:
		Cdata =loan_data.objects.filter(Agent_name=request.user)
	if request.user.is_superuser:
		Cdata =loan_data.objects.all()
		print(Cdata)
	return render(request,'view_data/Agent_Applications.html',{
		'title':title,'Cdata':Cdata})

#------------------------------------Super user to grant the loan-------------------------------

#Agent can see all the application
def pending(request):
	title='Pending Appication'
	if request.user.is_staff:
		Cdata =loan_data.objects.filter(Q(Agent_name=request.user) & Q(Approve='New'))
	if request.user.is_superuser:
		Cdata =loan_data.objects.filter(Approve='New')
	return render(request,'view_data/pending_applications.html',{
		'title':title,'Cdata':Cdata})
def info(request,id):
	Cdata=loan_data.objects.get(id=id)
	title='To Approve'
	return render(request,'view_data/to_approve.html',{
		'title':title,'Cdata':Cdata})


def updatee(request):
	id_val=request.GET['id']
	sta=request.GET['sta']
	Cdata = loan_data.objects.filter(id=id_val).update(Approve=sta)

	return redirect('pending')

#-----------------------------Agent to edit the application before approval------------------------

def edit_application(request,id):
	Cdata=loan_data.objects.get(id=id)
	title='Edit Appication'
	return render(request,'view_data/to_edit.html',{
		'title':title,'Cdata':Cdata})
def application_update(request):
	ida=request.GET['id_val']
	flag = False
	title='Edit applition'
	total_intrest=request.GET['total_intrest']
	total_amount=request.GET['total_amount']
	monthly=request.GET['monthly']
	amount=request.GET['loan_amount']
	year=request.GET['year']
	user_name=request.GET['user_name']
	user_name_error=' '
	a = re.findall(r'[0-9@!$%#*^]', user_name)
	if len(a) > 0:
		flag = True
		user_name_error = 'numbers, @, #, *, !, %, $, ^ are not vaild'
	first_name=request.GET['first_name']
	first_name_error=' '
	a = re.findall(r'[0-9@!$%#*^]', first_name)
	if len(a) > 0:
		flag = True
		first_name_error = 'numbers, @, #, *, !, %, $, ^ are not vaild'
	last_name=request.GET['last_name']
	last_name_error=' '
	a = re.findall(r'[0-9@!$%#*^]', last_name)
	if len(a) > 0:
		flag = True
		last_name_error = 'numbers, @, #, *, !, %, $, ^ are not vaild'
	email=request.GET['email']
	Address = request.GET['Address']
	Address_error = ' '
	a = re.findall(r'[@!$%]', Address)
	print(a)
	if len(a) > 0:
		flag = True
		Address_error = '@ , !, %, $, ^ are not vaild'
	adhaar_card=request.GET['adhaar_card']
	adhaar_card_error=' '
	p = request.GET['adhaar_card']
	if  len(p) != 12:
		flag = True
		adhaar_card_error = 'only 12 digits are valid'
	
	pan_card=request.GET['pan_card']
	pan_card_error=' '
	if  len(pan_card) != 10:
			flag = True
			pan_card_error = 'Invalid'
	phone_number=request.GET['phone_number']
	phone_number_error=' '
	p = request.GET['phone_number']
	if  len(p) != 10:
		flag = True
		phone_number_error = 'only 12 digits are valid'
	
	if flag==True:
		return render(request,'Form_base/apply_for_loan_error.html',{'loan_amount':amount,'year':year,
		'title':title,'first_name':first_name,'user_name':user_name,'email':email,
		'phone_number':phone_number,'pan_card':pan_card,'adhaar_card':adhaar_card,'Address':Address,'last_name':last_name,
		'phone_number_error':phone_number_error,'pan_card_error':pan_card_error,'adhaar_card_error':adhaar_card_error,
		'Address_error':Address_error,'last_name_error':last_name_error,'first_name_error':first_name_error,
		'user_name_error':user_name_error})
	else:
		Cdata = loan_data.objects.filter(id=ida).update(user_name=user_name,first_name=first_name,last_name=last_name,
			email=email,adhaar_card=adhaar_card,pan_card=pan_card,phone_number=phone_number,loan_amount=amount,monthly=monthly,
			year=year,total_interest=total_intrest,Address=Address)
		
		#print(datt)
		return redirect('index')






