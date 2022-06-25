from django.db import models

# Create your models here.
class Student(models.Model):
	name=models.CharField(max_length=30)
	rollnum=models.CharField(max_length=30)
	age=models.IntegerField()
	mobile=models.CharField(max_length=10)
	email=models.EmailField(max_length=30)
	address=models.TextField()

	def __str__(self):
		return self.name+' '+self.email

