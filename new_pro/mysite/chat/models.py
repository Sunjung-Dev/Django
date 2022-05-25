from django.db import models
from django.utils import timezone
 
# Create your models here.
class Post(models.Model):
    
    text = models.TextField()
    # 작성일자
    created_date = models.DateTimeField(default=timezone.now)
    
