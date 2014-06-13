from django.db import models

# Create your models here.
class checkin(models.Model):
	openId = models.CharField(max_length=50)
	checkin_date = models.DateField(auto_now_add=True)
	checkin_time = models.TimeField(auto_now_add=True)	

	def __unicode__(self):
		return self.openId