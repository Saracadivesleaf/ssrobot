from django.db import models

# Create your models here.
class messages(models.Model):
	
    openId = models.CharField(max_length=50)
    msg = models.TextField()
    receive_date = models.DateField(auto_now_add=True)
    receive_time = models.TimeField(auto_now_add=True)

    def __unicode__(self):
        return self.openId