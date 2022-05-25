from django.db import models
 
class Info(models.Model):
    content_text = models.CharField(max_length=200)
    create_date = models.DateTimeField('date published')
