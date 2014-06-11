from django.db import models

# Create your models here.
class board_content(models.Model):

#   id = models.AutoField(primary_key=True)
    msg = models.TextField()
#    from_user = models.CharField(max_length=100, null=true)
    receive_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.msg