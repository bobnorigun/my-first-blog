from django.db import models

# Create your models here.
class Profile(models.Model):
	name = models.CharField(max_length=150)
	email = models.EmailField(blank=True)
	address = models.CharField(max_length=150)
	phone = models.CharField(max_length=150,unique=True) # unique는 중복되면 에러?
	profile = models.TextField()

	def __str__(self):
		return self.name