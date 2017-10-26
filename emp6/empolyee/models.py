from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse
class Registers(models.Model):
	em_name = models.CharField(max_length=250)
	em_father_mother_name = models.CharField(max_length=250)
	em_dob = models.CharField(max_length=250)
	em_address = models.CharField(max_length=250)
	em_aadher_number = models.CharField(max_length=150)
	em_mobile = models.CharField(max_length=250)
	em_email = models.CharField(max_length=250)
	em_alternate_no = models.CharField(max_length=250)
	em_type = models.CharField(max_length=150)
	
	def get_absolute_url(self):
		return reverse('empolyee:detail',kwargs={'pk':self.pk})

	def __str__(self):
		return self.em_name

class Employees(models.Model):
	name = models.CharField(max_length=250)
	dob = models.CharField(max_length=250)
	address = models.CharField(max_length=250)
	mobile = models.CharField(max_length=2500)
	email = models.CharField(max_length=2500)
	alternate_no = models.CharField(max_length=250)
	date_join = models.CharField(max_length=250)
	post = models.CharField(max_length=250)
	type1 = models.CharField(max_length=250)
	dep = models.CharField(max_length=250)
	remarks = models.CharField(max_length=2500)
	def __str__(self):
		return self.name+ "--"+self.dep

class Leaves(models.Model):
	em_id = models.CharField(max_length=250)
	em_name = models.CharField(max_length=250)
	department = models.CharField(max_length=250)
	leave_from = models.CharField(max_length=250)
	leave_to = models.CharField(max_length=250)
	no_days = models.CharField(max_length=250)
	reason = models.CharField(max_length=250)
	status = models.CharField(max_length=250)
	def __str__(self):
		return self.em_name

class Payments(models.Model):
	emp_id = models.CharField(max_length=250)
	name = models.CharField(max_length=250)
	department = models.CharField(max_length=250)
	mounth = models.CharField(max_length=250)
	leaves_no_days = models.CharField(max_length=250)
	actual_ctc = models.CharField(max_length=250)
	payble_ctc = models.CharField(max_length=250)
	def __str__(self):
		return self.name


class Users(models.Model):
	
	name = models.CharField(max_length=250)
	email = models.CharField(max_length=250)
	username = models.CharField(max_length=250)
	password = models.CharField(max_length=250)
	
	def __str__(self):
		return self.name



class Admins(models.Model):
	name = models.CharField(max_length=250)
	email = models.CharField(max_length=250)
	username = models.CharField(max_length=250)
	password = models.CharField(max_length=250)
	def __str__(self):
		return self.name

