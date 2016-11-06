from django.db import models
from django.core.urlresolvers import reverse

class Student(models.Model):
	s_id = models.AutoField(primary_key=True)
	s_name = models.CharField(max_length=30)
	s_dob = models.DateField()
	s_email = models.EmailField(max_length=100, null=True, blank=True, unique=True)
	s_mobile = models.IntegerField()
	s_address = models.CharField(max_length=30)

	def get_absolute_url(self):
		return reverse('update', kwargs={'pk': self.pk})

class Course(models.Model):
	c_code = models.AutoField(primary_key=True)
	c_name = models.CharField(max_length=30)
	t_id = models.IntegerField()
	c_status = models.BooleanField(default=True)

class Teacher(models.Model):
	t_id = models.AutoField(primary_key=True)
	t_name = models.CharField(max_length=30)
	t_age = models.IntegerField()
	t_qual = models.CharField(max_length=30)

class Registration(models.Model):
	r_id = models.AutoField(primary_key=True)
	s_name = models.CharField(max_length=30)
	s_dob = models.DateField()
	s_email = models.EmailField(max_length=70, null=True, blank=True, unique=True)
	s_mobile = models.IntegerField()
	s_address = models.CharField(max_length=30)
