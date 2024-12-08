from django.db import models

# Create your models here.
class Diary(models.Model):
    date= models.DateTimeField (auto_now_add= True)
    Title= models.CharField(max_length=50)
    description= models.TextField()
    
    def __str__(self):
        return self.date
