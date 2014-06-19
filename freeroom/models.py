from django.db import models

# Create your models here.
class query_result(models.Model):
	# Basic Attribute
	open_id = models.CharField(max_length=50)
	query_date = models.DateField(auto_now_add=True)
	
	# Query Parameters
	date = models.DateField()
	building = models.AutoField()
	from_class = models.IntegerField()
	to_class = models.IntegerField()

	# Query Result
	result = models.TextField()

	def __unicode__(self):
		str = '%s @ %s (Queried on %s)' % (self.building, self.date, self.query_date)
		return str



class buildings(models.Model):
	name = models.CharField(max_length=10)

	def __unicode__(self):
		return self.name