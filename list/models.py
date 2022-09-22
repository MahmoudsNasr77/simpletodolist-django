from xmlrpc.client import DateTime, boolean
from django.db import models
class list(models.Model):
    Tode_item=models.CharField(max_length=1000,verbose_name="المهمه")
    date=models.DateTimeField(auto_now=True)
    hour=models.IntegerField(default=0,verbose_name="عدد ساعات")
    minute=models.IntegerField(default=0,verbose_name="عدد دقائق")
    class Meta:
        verbose_name = 'المهام'

       

