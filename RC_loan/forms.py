from django import forms
from django.contrib.auth.models import User
from RC_loan.models import Agent_block,customer_block
from django.contrib.auth.forms import UserCreationForm


class Agent_block(UserCreationForm):
	class Meta:
		model=User
		fields=(
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2',
			)
	def save(self,commit=True):
		user=super(Agent_block,self).save(commit=False)
		user.first_name=self.cleaned_data['first_name']
		user.last_name=self.cleaned_data['last_name']
		user.email=self.cleaned_data['email']
		user.is_staff = True
		if commit:
			user.save()
		return user

class RegistrationForm(UserCreationForm):

	class Meta:
		model=User
		fields=(
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2',
			)

		widgets = {
			'username': forms.TextInput(attrs={'class': 'form-control-input','style':'font-size:17px;'}),
			'first_name':forms.TextInput(attrs={'class': 'form-control-input','style':'font-size:17px;'}),
			'last_name':forms.TextInput(attrs={'class': 'form-control-input','style':'font-size:17px;'}),
			'email':forms.TextInput(attrs={'class': 'form-control-input','style':'font-size:17px;'}),
			'password1':forms.PasswordInput(attrs={'class': 'form-control-input','style':'font-size:17px;'}),
			'password2': forms.PasswordInput(attrs={'class': 'form-control-input ','style':'font-size:17px;'}),
		}

	def save(self,commit=True):
		user=super(RegistrationForm,self).save(commit=False)
		user.first_name=self.cleaned_data['first_name']
		user.last_name=self.cleaned_data['last_name']
		user.email=self.cleaned_data['email']
		if commit:
			user.save()
		return user




'''class customer_block(forms.ModelForm):

	class Meta:
		model=customer_block
		fields=(
			'user',
			'Date_of_birth',
			'Address',
			'city',
			'Phone_number',
			)
	def save(self,commit=True):
		user=super(FresherForm,self).save(commit=False)
		user.Date_of_birth=self.cleaned_data['Date_of_birth']
		user.Address=self.cleaned_data['Address']
		user.city=self.cleaned_data['city']
		user.Phone_number=self.cleaned_data['Phone_number']


		if commit:
			def create_profilee(sender, **kwargs):
				if kwargs['created']:
					Employee.objects.create(user=kwargs['instance'])
			post_save.connect(create_profilee, sender=User)
			user.save()
		return user'''
