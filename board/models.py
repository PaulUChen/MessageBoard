from django.db import models
# Create your models here.
class BoardMessage(models.Model):
    title = models.CharField(max_length=20,null=False,blank=False)
    content = models.TextField(null=False,blank=False)
    date = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=20,default='')
    def __str__(self):
        return self.title