from django.db import models

class Contact(models.Model):    
    name=models.CharField(max_length=60)
    email=models.EmailField(blank=True,null=True)
    no=models.CharField(max_length=13)
    msg=models.TextField()
    address=models.TextField()

    def __str__(self):
        return self.name

class Slider(models.Model):
    name=models.CharField(max_length=60)
    img=models.ImageField(upload_to='slider/')
