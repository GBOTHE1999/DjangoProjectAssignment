from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255,)
    weight=models.FloatField()
    price=models.FloatField()
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.user) +' , '+self.name +' , '+ str(self.weight)+' , '+ str(self.price)+' , '+str(self.created_at) +' , '+ str(self.updated_at)
    
    def get_absolute_url(self):
        return reverse('product-list')
# Create your models here.
