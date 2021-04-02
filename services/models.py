from django.db import models

class Services(models.Model):
    alignChoice=[
        ('l','Left'),
        ('r','Right')
    ]
    name=models.CharField(max_length=60)
    desc=models.TextField()
    align=models.CharField(max_length=10,choices=alignChoice)
    img=models.ImageField(null=True, blank=True, upload_to='services/')

    def __str__(self):
        return self.name
