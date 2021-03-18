from django.db import models
from services.models import Services

class Photos(models.Model):
    widthChoice=[
        ('0','4x1'),
        ('width-1','3x1'),
        ('width-2','2x1')
    ]
    name=models.CharField(max_length=60)
    desc=models.TextField()
    width=models.CharField(max_length=10,choices=widthChoice)
    img=models.ImageField(upload_to='photos/')
    category=models.OneToOneField(Services,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
