from django.db import models



class Test_Table(models.Model):
    
    ts = models.DateTimeField(primary_key=True, auto_now_add=True)
    text = models.TextField(null=True)