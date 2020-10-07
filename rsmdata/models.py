from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

class Registration(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	phone_no = models.CharField(max_length=10)
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=200)


class Employee(models.Model):
	full_name = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	phone_no = PhoneNumberField()
	address = models.CharField(max_length=250)
	skills = models.CharField(max_length=300)
	pincode = models.CharField(max_length=8)
	dob = models.DateField()
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	marital_status = models.CharField(max_length=10)
	
	def __str__(self):
		return self.full_name


class Education(models.Model):
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
	education = models.CharField(max_length=100)
	board = models.CharField(max_length=100)
	passing_out_year = models.CharField(max_length=50)
	university = models.CharField(max_length=200)
	course = models.CharField(max_length=100)
	specification = models.CharField(max_length=200)
	percent = models.CharField(max_length=150)


class Certifications(models.Model):
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
	certification_name = models.CharField(max_length=300)
	certificatio_body = models.TextField()
	year = models.CharField(max_length=20)