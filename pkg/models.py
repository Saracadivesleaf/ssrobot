from django.db import models

# Create your models here.
class Package(models.Model):
	name = models.CharField(max_length=20)
	key_word = models.CharField(max_length=5)
	status = models.BooleanField(default=True)

	def __unicode__(self):
		return self.key_word