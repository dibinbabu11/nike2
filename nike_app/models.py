from django.db import models

# Create your models here.
class Nikeshoe(models.Model):
    name=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.CharField(max_length=250)
    image=models.ImageField( upload_to='media/')
    stock=models.IntegerField()
    
    def __str__(self):
        return self.name
    