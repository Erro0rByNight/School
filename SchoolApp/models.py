from django.db import models

# Create your models here.
class Class(models.Model):
	"""This Model represent all class at list."""
	name = models.CharField(max_length=35)
	branches = models.CharField(max_length=25)
	teachers = models.CharField(max_length=500)

	def __str__(self):
		"""represents the name of the object."""
		return self.name


