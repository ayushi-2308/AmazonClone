from django.db import models

# Create your models here.
class Mediaa(models.Model):
    obj1=models.CharField(max_length=90)
    obj2=models.FileField(upload_to='Media/',default=None,null=True)