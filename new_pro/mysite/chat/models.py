from django.db import models
from django.utils import timezone
 
# Create your models here.
class Post(models.Model):
    
    text = models.TextField()
    # μμ±μΌμ
    created_date = models.DateTimeField(default=timezone.now)
    
