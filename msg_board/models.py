from django.db import models

# Create your models here.
class board_content(models.Model):
	
    msg = models.TextField()
    receive_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.msg